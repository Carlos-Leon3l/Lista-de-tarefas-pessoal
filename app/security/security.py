from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_current_user(
    # parei em criar usuario atual
):
    pass