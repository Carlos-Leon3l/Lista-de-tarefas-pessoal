from fastapi import FastAPI, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
import jwt

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme(Depends)


def get_current_user(token: str = Depends(oauth2_scheme)):
    return {"token": token}
