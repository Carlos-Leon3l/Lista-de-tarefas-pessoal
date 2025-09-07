from fastapi import FastAPI, HTTPException
from models import tables


def login(email: str, senha:str):
    if not email or not senha:
        raise HTTPException(status_code=400, detail="Os campos email e senha sao obrigatorios as serem preenchidos")
    
    email_usuario_banco = tables.get_user_by_email(email)
    if not email_usuario_banco:
        return HTTPException(status_code=400, detail="Email do usuario nao cadastrdo no sistema")
    
    
    senha_hash = email_usuario_banco.get("password")
    if not senha_hash:
        raise HTTPException(status_code="404", detail="senha não encontrada, ou não compativel")
    
    
    