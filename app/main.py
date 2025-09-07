from fastapi import FastAPI
from routes import (rotas_lista_tarefa, rotas_user)
import os

SECRET_KEY= "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

app = FastAPI()
app.include_router(rotas_lista_tarefa.router)
app.include_router(rotas_user.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)