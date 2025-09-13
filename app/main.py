from fastapi import FastAPI
from routes import (rotas_lista_tarefa, rotas_user)
import os




app = FastAPI()
app.include_router(rotas_lista_tarefa.router)
app.include_router(rotas_user.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)