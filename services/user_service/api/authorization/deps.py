from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from services.user_service.common.consts import ALGORITHM
from services.user_service.api.authorization.secret import JWT_SECRET_KEY 
from services.user_service.common.abstract import User, TokenPayload
from services.user_service.business_logic.db_connectors import get_user as __get_user
from services.user_service.common.consts import JWT_DATEFMT

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


async def get_current_user(token: str = Depends(reuseable_oauth)) -> User:
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(expires_delta=payload["expires_delta"], login=payload["login"])

        if datetime.strptime(token_data.expires_delta, JWT_DATEFMT) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await __get_user(token_data.login, check=True)
