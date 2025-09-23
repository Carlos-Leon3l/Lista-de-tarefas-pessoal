from fastapi import FastAPI
from routes import (rotas_lista_tarefa, rotas_user)
from fastapi.middleware.cors import CORSMiddleware
import os

origins = [ 
    "http://127.0.0.1:8001"
    "http://127.0.0.1:8080"
    ]

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"])

app.include_router(rotas_lista_tarefa.router)
app.include_router(rotas_user.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)