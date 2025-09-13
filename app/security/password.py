from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_for_hashed(user_password: str) -> str:
    return pwd_context.hash(user_password)

def verificar_senha_hash(password_atual:str, password_hashed:str) -> bool:
    return pwd_context.verify(password_atual, password_hashed)
    