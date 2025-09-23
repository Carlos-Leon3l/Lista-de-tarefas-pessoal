from fastapi import HTTPException
from models import tables
from security.token import gerar_token
from security.password import verificar_senha_hash


def login(email: str, password:str):
    if not email or not password:
        raise HTTPException(status_code=400, detail="Os campos email e senha sao obrigatorios as serem preenchidos")
    
    email_usuario_banco = tables.get_user_by_email(email)
    if not email_usuario_banco:
        return HTTPException(status_code=400, detail="Email do usuario nao cadastrdo no sistema")
    
    
    senha_hash = email_usuario_banco.get("password")
    if not verificar_senha_hash(password, senha_hash):
        print(verificar_senha_hash(password, senha_hash))
        raise HTTPException(status_code=401, detail="senha não encontrada, ou não compativel")
    
    usuario_id = email_usuario_banco.get("id")
    if usuario_id == None:
        raise HTTPException(status_code=400, detail="id do usuario nao encontrado")
    
    
    jwt = gerar_token(  
        usuario_id= usuario_id,
        email=email
    )
    return jwt
    
    