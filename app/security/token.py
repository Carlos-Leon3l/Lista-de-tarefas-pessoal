import jwt

SECRET_KEY= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def gerar_token(usuario_id:int, email:str ):
    payload = {
        "usuario_id": usuario_id,
        'email': email
    }
    
    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    print(f"Token gerado para o usuário {email}: {token}")
    
    return token