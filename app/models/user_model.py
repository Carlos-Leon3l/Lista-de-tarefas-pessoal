from pydantic import BaseModel

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    
class LoginRequest(BaseModel):
    email: str
    password: str
    
class UserCreate(RegisterRequest):
    id: int
    class Config:
        from_attributes = True
        
class TokenPayload(BaseModel):
    usuario_id: int

# Teste de criação Auth2
# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str
    

    
    