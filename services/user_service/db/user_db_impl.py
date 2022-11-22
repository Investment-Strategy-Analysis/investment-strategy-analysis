from typing import Optional
import logging
from services.user_service.common.abstract import Email, User, Password, Photo, Settings, UserSettings
from services.user_service.common.helpers import db_session, db_engine
from services.user_service.db.tables import Base
from services.user_service.api.authorization.utils import get_hashed_password
import services.user_service.db.tables as T
from services.common.helpers import to_analysis_time

__engine = db_engine()
__session = db_session(__engine)
Base.metadata.create_all(__engine)  # create tables if not exists


def __analysis_time_int(analysis_time):
    if isinstance(analysis_time, str):
        return to_analysis_time(analysis_time).value.days
    else:
        return analysis_time


def get_user_by_login(login: str) -> Optional[User]:
    user = __session.get(T.User, login)
    if user is None:
        return None
    else:
        res_user = user.to_pydantic()
        return res_user


def save_user(user: User):
    new_user = __session.query(T.User).filter(T.User.login == user.login).first()
    assert new_user is None, "user already exists"
    last_answer = T.LastAnswer()
    __session.add(last_answer)
    user_settings = T.UserSettings(
        email=user.user_settings.email,
        last_answer=last_answer
    )
    __session.add(user_settings)
    restrictions = T.Restriction(
        target_profit=user.settings.restrictions.target_profit,
        checkboxes=user.settings.restrictions.checkboxes,
        upper_border=user.settings.restrictions.upper_border,
        lower_border=user.settings.restrictions.lower_border,
        analysis_time=__analysis_time_int(user.settings.restrictions.analysis_time))
    __session.add(restrictions)
    settings = T.Settings(
        strategy=user.settings.strategy,
        restrictions=restrictions,
        risk=user.settings.risk)
    __session.add(settings)
    _user = T.User(
        login=user.login,
        password=user.password,
        settings=settings,
        user_settings=user_settings)
    __session.add(_user)
    __session.commit()
    logging.info(f"saved user with login={user.login}")


def update_settings(login: str, settings: Settings):
    user = __session.query(T.User).filter(T.User.login == login).first()
    user.settings.restrictions.target_profit = settings.restrictions.target_profit
    user.settings.restrictions.checkboxes = settings.restrictions.checkboxes
    user.settings.restrictions.upper_border = settings.restrictions.upper_border
    user.settings.restrictions.lower_border = settings.restrictions.lower_border
    user.settings.restrictions.analysis_time = __analysis_time_int(settings.restrictions.analysis_time)
    user.settings.strategy = settings.strategy
    user.settings.risk = settings.risk
    __session.add(user)
    __session.commit()
    logging.info(f"updated settings, login={login}")


def update_user_settings(login: str, user_settings: UserSettings):
    user = __session.query(T.User).filter(T.User.login == login).first()
    # assert user_settings.last_answer is None, "last answer can't update"  FIXME
    user.user_settings.photo = user_settings.photo
    user.user_settings.email = user_settings.email
    __session.add(user)
    __session.commit()
    logging.info(f"updated user_settings, login={login}")


def update_user_email(login: str, email: Email):
    user = __session.query(T.User).filter(T.User.login == login).first()
    user.user_settings.email = email.email
    __session.add(user)
    __session.commit()
    logging.info(f"updated email, login={login}")


def update_user_password(login: str, password: Password):
    user = __session.query(T.User).filter(T.User.login == login).first()
    user.password = get_hashed_password(password.password)
    __session.add(user)
    __session.commit()
    logging.info(f"updated password, login={login}")


def update_user_photo(login: str, photo: Photo):
    user = __session.query(T.User).filter(T.User.login == login).first()
    user.user_settings.photo = photo.photo
    __session.add(user)
    __session.commit()
    logging.info(f"updated photo, login={login}")


def delete_user_by_login(login: str):
    user = __session.get(T.User, login)
    if user is None:
        logging.error(f"user with login={login} not exist")
    else:
        __session.delete(user)
        __session.commit()
        logging.info(f"deleted user with login={login}")
