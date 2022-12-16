import os
from typing import Optional, List
import logging
from services.user_service.common.abstract import Email, User, Password, Photo, Settings, UserSettings
from services.user_service.common.consts import ADMIN
from services.user_service.common.helpers import db_session, db_engine
from services.user_service.db.tables import Base
from services.user_service.api.authorization.utils import get_hashed_password
import services.user_service.db.tables as T

__engine = db_engine()
session = db_session(__engine)
Base.metadata.create_all(__engine)  # create tables if not exists
T.session = session


def get_user_by_login(login: str) -> Optional[User]:
    user = session.get(T.User, login)
    if user is None:
        return None
    else:
        res_user = user.to_pydantic()
        return res_user


def save_user(user: User):
    new_user = session.query(T.User).filter(T.User.login == user.login).first()
    assert new_user is None, "user already exists"
    last_answer = T.LastAnswer()
    session.add(last_answer)
    user_settings = T.UserSettings(
        email=user.user_settings.email,
        last_answer=last_answer
    )
    session.add(user_settings)
    restrictions = T.Restriction(
        target_profit=user.current_settings.restrictions.target_profit,
        checkboxes=user.current_settings.restrictions.checkboxes,
        upper_border=user.current_settings.restrictions.upper_border,
        lower_border=user.current_settings.restrictions.lower_border,
        analysis_time=user.current_settings.restrictions.analysis_time)
    session.add(restrictions)
    current_settings = T.Settings(
        strategy=user.current_settings.strategy,
        restrictions=restrictions,
        risk=user.current_settings.risk)
    session.add(current_settings)
    _user = T.User(
        login=user.login,
        password=user.password,
        current_settings=current_settings,
        settings=[],
        user_settings=user_settings)
    session.add(_user)
    session.commit()
    logging.info(f"saved user with login={user.login}")


def save_from_current_settings(login: str):
    user = session.query(T.User).filter(T.User.login == login).first()
    restrictions = T.Restriction(
        target_profit=user.current_settings.restrictions.target_profit,
        checkboxes=user.current_settings.restrictions.checkboxes,
        upper_border=user.current_settings.restrictions.upper_border,
        lower_border=user.current_settings.restrictions.lower_border,
        analysis_time=user.current_settings.restrictions.analysis_time)
    session.add(restrictions)
    saved_current_settings = T.Settings(
        strategy=user.current_settings.strategy,
        restrictions=restrictions,
        risk=user.current_settings.risk)
    session.add(saved_current_settings)
    session.commit()
    user.settings = [*user.settings, saved_current_settings.id]
    session.add(user)
    session.commit()
    logging.info(f"save current_settings to settings, login={login}")


def reset_settings(login: str, settings: List[Settings]):
    user = session.query(T.User).filter(T.User.login == login).first()
    for id in user.settings:
        session.delete(session.get(T.Settings, id))
    settings_new = []
    for settings_i in settings:
        restrictions = T.Restriction(
            target_profit=settings_i.restrictions.target_profit,
            checkboxes=settings_i.restrictions.checkboxes,
            upper_border=settings_i.restrictions.upper_border,
            lower_border=settings_i.restrictions.lower_border,
            analysis_time=settings_i.restrictions.analysis_time)
        session.add(restrictions)
        saved_settings_i = T.Settings(
            strategy=settings_i.strategy,
            restrictions=restrictions,
            risk=settings_i.risk)
        session.add(saved_settings_i)
        settings_new.append(saved_settings_i)
    session.commit()
    user.settings = list(map(lambda x: x.id, settings_new))
    session.add(user)
    session.commit()
    logging.info(f"save current_settings to settings, login={login}")


def update_current_settings(login: str, settings: Settings):
    user = session.query(T.User).filter(T.User.login == login).first()
    user.current_settings.restrictions.target_profit = settings.restrictions.target_profit
    user.current_settings.restrictions.checkboxes = settings.restrictions.checkboxes
    user.current_settings.restrictions.upper_border = settings.restrictions.upper_border
    user.current_settings.restrictions.lower_border = settings.restrictions.lower_border
    user.current_settings.restrictions.analysis_time = settings.restrictions.analysis_time
    user.current_settings.strategy = settings.strategy
    user.current_settings.risk = settings.risk
    session.add(user)
    session.commit()
    logging.info(f"updated current_settings, login={login}")


def update_user_settings(login: str, user_settings: UserSettings):
    user = session.query(T.User).filter(T.User.login == login).first()
    # assert user_settings.last_answer is None, "last answer can't update"  FIXME
    user.user_settings.photo = user_settings.photo
    user.user_settings.email = user_settings.email
    session.add(user)
    session.commit()
    logging.info(f"updated user_settings, login={login}")


def update_user_email(login: str, email: Email):
    user = session.query(T.User).filter(T.User.login == login).first()
    user.user_settings.email = email.email
    session.add(user)
    session.commit()
    logging.info(f"updated email, login={login}")


def update_user_password(login: str, password: Password):
    user = session.query(T.User).filter(T.User.login == login).first()
    user.password = get_hashed_password(password.password)
    session.add(user)
    session.commit()
    logging.info(f"updated password, login={login}")


def update_user_photo(login: str, photo: Photo):
    user = session.query(T.User).filter(T.User.login == login).first()
    user.user_settings.photo = photo.photo
    session.add(user)
    session.commit()
    logging.info(f"updated photo, login={login}")


def delete_user_by_login(login: str):
    user = session.get(T.User, login)
    if user is None:
        logging.error(f"user with login={login} not exist")
    else:
        session.delete(user)
        session.commit()
        logging.info(f"deleted user with login={login}")


try:
    save_user(User(login=ADMIN, password=get_hashed_password(os.environ["ADMIN_PASS"])))
except:
    pass
