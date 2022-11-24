from typing import Optional
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, ARRAY, Float
from sqlalchemy.orm import declarative_base, relationship
import services.user_service.common.abstract as A

session = None


class BasePydantic:
    def to_pydantic(self):
        pass


Base = declarative_base(cls=BasePydantic)


def _get_pydantic(base_obj: Optional[BasePydantic]) -> Optional[BaseModel]:
    if base_obj is None:
        return None
    return base_obj.to_pydantic()


class Restriction(Base):
    __tablename__ = "restrictions"
    id = Column(Integer, primary_key=True)
    target_profit = Column("target_profit", Float, nullable=False, default=0.)
    checkboxes = Column("checkboxes", JSON, nullable=False, default=dict())
    upper_border = Column("upper_border", JSON)
    lower_border = Column("lower_border", JSON)
    analysis_time = Column("analysis_time", Integer, nullable=False, default=0)

    settings_id = Column("settings_id", Integer, ForeignKey("settings.id"))

    def __repr__(self):
        return f"Restriction(id={self.id}, target_profit={self.target_profit}, checkboxes={self.checkboxes}, " \
               f"upper_border={self.upper_border}, lower_border={self.lower_border}, analysis_time={self.analysis_time})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        return A.Restriction(target_profit=self.target_profit, checkboxes=self.checkboxes, upper_border=self.upper_border,
                      lower_border=self.lower_border, analysis_time=self.analysis_time)


class Settings(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    strategy = Column("strategy", String, nullable=False, default="default")
    restrictions = relationship("Restriction", uselist=False)
    risk = Column("risk", Float, nullable=False, default=0)

    last_answer_id = Column("last_answer_id", Integer, ForeignKey("last_answers.id"))
    user_login = Column("user_login", String, ForeignKey("users.login"))

    def __repr__(self):
        return f"Settings(id={self.id}, strategy={self.strategy}, restrictions={self.restrictions}, risk={self.risk})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        return A.Settings(strategy=self.strategy, restrictions=_get_pydantic(self.restrictions), risk=self.risk)


class LastAnswer(Base):
    __tablename__ = "last_answers"
    id = Column(Integer, primary_key=True)
    result = Column("result", ARRAY(Float, dimensions=1))
    settings = relationship("Settings", uselist=False)

    user_settings_id = Column("user_settings_id", Integer, ForeignKey("user_settings.id"))

    def __repr__(self):
        return f"LastAnswer(id={self.id}, result={self.result}, settings={self.settings})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        return A.LastAnswer(result=self.result, settings=_get_pydantic(self.settings))


class UserSettings(Base):
    __tablename__ = "user_settings"
    id = Column(Integer, primary_key=True)
    last_answer = relationship("LastAnswer", uselist=False)
    photo = Column("photo", String)     # FIXME(bytes)
    email = Column("email", String)

    user_login = Column("user_login", String, ForeignKey("users.login"))

    def __repr__(self):
        return f"UserSettings(id={self.id}, last_answer={_get_pydantic(self.last_answer)}, email={self.email})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        return A.UserSettings(last_answer=_get_pydantic(self.last_answer), photo=self.photo, email=self.email)


class User(Base):
    __tablename__ = "users"
    login = Column("login", String, primary_key=True)
    password = Column("password", String, nullable=False)   # hash
    current_settings = relationship("Settings", uselist=False)
    settings = Column("current_settings_ids", ARRAY(Integer, dimensions=1))
    user_settings = relationship("UserSettings", uselist=False)

    def __repr__(self):
        return f"User(login={self.login}, current_settings={self.current_settings}, user_settings={self.user_settings})"

    def __str__(self):
        return self.__repr__()

    def to_pydantic(self):
        settings = []
        for id in self.settings:
            settings.append(_get_pydantic(session.get(Settings, id)))
        return A.User(login=self.login, password=self.password, current_settings=_get_pydantic(self.current_settings), settings=settings, user_settings=_get_pydantic(self.user_settings))
