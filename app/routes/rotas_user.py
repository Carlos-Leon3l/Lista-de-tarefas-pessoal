from fastapi import APIRouter, HTTPException
from models.user_model import RegisterRequest, UserCreate
from models import tables
from security.password import get_password_for_hashed

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

@router.post("/login")
def rota_login():
    pass

@router.get("/usuario/{id}", response_model=UserCreate, status_code=200)
def return_user_by_id(usuario_id: int):
    
    db_usuario = tables.get_user_by_id(usuario_id)
    print(f"recebendo o id: {db_usuario}")
    if(db_usuario is None):
        raise HTTPException(status_code=404, detail="Usuario não encontrado") 

    return db_usuario