from fastapi import FastAPI
from routes import (rotas_lista_tarefa, rotas_user)
from fastapi.middleware.cors import CORSMiddleware
import os

origins = [ 
    "http://127.0.0.1:8001"
    "http://localhost:5173"
    ]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Permite as origens listadas
    allow_credentials=True, # Permite cookies/credenciais
    allow_methods=["*"],    # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],    # Permite todos os cabeçalhos
)

app.include_router(rotas_lista_tarefa.router)
app.include_router(rotas_user.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)