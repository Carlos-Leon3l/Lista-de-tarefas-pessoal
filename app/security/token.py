from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from models.user_model import TokenPayload
from pydantic import ValidationError

security = HTTPBearer()

SECRET_KEY= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def gerar_token(usuario_id:int, email:str ):
    payload = {
        "usuario_id": usuario_id,
        'email': email
    }
    
    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    print(f"Token gerado para o usuário com id {usuario_id} e email: {email}, Token: {token}")
    
    return token 

def verificar_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token invalido")

async def get_current_user(token_credentials: HTTPAuthorizationCredentials = Depends(security)):
    
    token = token_credentials.credentials
    try:
        payload = verificar_token(token)
        print("verificando_token:", payload)
        token_data = TokenPayload(**payload)
        print("printando token_data",token_data)
        return token_data
    except ValidationError as e:
        raise HTTPException(status_code=401, detail=f"credenciais invalidas {e}")
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
