from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from services.user_service.api.authorization.secret import *
from services.user_service.common.consts import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES, ALGORITHM
from services.user_service.common.abstract import TokenPayload

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str, pass_hashed: bool = False) -> bool:
    if pass_hashed:
        return password == hashed_pass
    return password_context.verify(password, hashed_pass)


def create_access_token(login: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    payload = TokenPayload(expires_delta=str(expires_delta), login=login)
    encoded_jwt = jwt.encode(payload.dict(), JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(login: str, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    payload = TokenPayload(expires_delta=str(expires_delta), login=login)
    encoded_jwt = jwt.encode(payload.dict(), JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt
