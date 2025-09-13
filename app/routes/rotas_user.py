from fastapi import APIRouter, HTTPException
from models.user_model import RegisterRequest, UserCreate, LoginRequest
from models import tables
from security.password import get_password_for_hashed
from security.token import gerar_token
from controllers.controller_login import login
import bcrypt

router = APIRouter()

tables.criar_tabela()

@router.post("/register", status_code=201)
def register_user(user: RegisterRequest):
    
    existing_user = tables.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario com esse email ja existe") 
    
    senha_hash = get_password_for_hashed(user.password)
    tables.create_user(user.username, user.email, senha_hash)
    
    return  ({
        "username": user.username,
        "email": user.email,
        "password": senha_hash
    })

@router.post("/login", status_code=201)
def rota_login(request: LoginRequest):
    result_token = login(request.email, request.password)
    
    if not result_token:
        raise HTTPException(status_code=404, detail="credenciais invalidas", headers={"WWW-Authenticate":"Bearer"})
    
    return {"message": "Login Bem-Sucedido",
            "access-token": result_token}
    

@router.get("/usuario/{id}", response_model=UserCreate, status_code=200)
def return_user_by_id(usuario_id: int):
    
    db_usuario = tables.get_user_by_id(usuario_id)
    print(f"recebendo o id: {db_usuario}")
    if(db_usuario is None):
        raise HTTPException(status_code=404, detail="Usuario não encontrado") 

    return db_usuario


"""
CONTA TESTE LOGIN
{
  "username": "carlos123",
  "email": "carlos1@gmail.com",
  "password": "12345678"
}
"""