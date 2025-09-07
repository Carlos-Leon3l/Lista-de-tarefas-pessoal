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
    