from typing import Optional
from services.user_service.common.abstract import User
import logging
from services.user_service.common.helpers import db_session, db_engine
from services.user_service.db.tables import Base
import services.user_service.db.tables as T

__engine = db_engine()
__session = db_session(__engine)
Base.metadata.create_all(__engine)  # create tables if not exists


# not update now
def save_user(user: User):
    new_user = __session.query(T.User).filter(T.User.login == user.login).first()
    if new_user is not None:
        logging.info("skip")
        return
    last_answer = T.LastAnswer()
    __session.add(last_answer)
    __session.flush()
    __session.refresh(last_answer)
    user_settings = T.UserSettings(
        last_answer=last_answer)
    __session.add(user_settings)
    __session.flush()
    __session.refresh(user_settings)
    restrictions = T.Restriction(
        target_profit=user.settings.restrictions.target_profit,
        checkboxes=user.settings.restrictions.checkboxes,
        upper_border=user.settings.restrictions.upper_border,
        lower_border=user.settings.restrictions.lower_border,
        analysis_time=user.settings.restrictions.analysis_time)
    __session.add(restrictions)
    __session.flush()
    __session.refresh(restrictions)
    settings = T.Settings(
        strategy=user.settings.strategy,
        restrictions=restrictions,
        risk=user.settings.risk)
    __session.add(settings)
    __session.flush()
    __session.refresh(settings)
    _user = T.User(
        login=user.login,
        password=user.password,
        settings=settings,
        user_settings=user_settings)
    __session.add(_user)
    __session.flush()
    __session.refresh(_user)
    __session.commit()
    logging.info(f"saved user with login={user.login}")


def get_user_by_login(login: str) -> Optional[User]:
    user = __session.get(T.User, login)
    if user is None:
        return None
    else:
        return user.to_pydantic()


def delete_user_by_login(login: str):
    user = __session.get(T.User, login)
    if user is None:
        logging.error(f"user with login={login} not exist")
    else:
        __session.delete(user)
        __session.commit()
        logging.info(f"deleted user with login={login}")
