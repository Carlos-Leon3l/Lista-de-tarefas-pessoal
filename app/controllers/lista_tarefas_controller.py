from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import tables

templates = Jinja2Templates(directory="templates")

tables.criar_tabela()

def mostrar_tarefa(request:Request):
    tarefas = tables.listar_tarefas()
    return templates.TemplateResponse("index.html" ,{ "request": request, "tarefas": tarefas })

def mostrar_edicao(request:Request , tarefa_id:int):
    tarefa = tables.buscar_tarefa_por_id(tarefa_id)
    tarefas = tables.listar_tarefas()
    return templates.TemplateResponse("Listagem/editar.html", {
        "request": request, "tarefa":tarefa, "tarefas":tarefas}
        )

async def adicionar_tarefa(request:Request, tarefa: str = Form(...)):
    tables.inserir_tarefa(tarefa)
    return RedirectResponse("/", status_code=303)

def excluir_tarefa(tarefa_id:int):
    tables.excluir_tarefa(tarefa_id)
    return RedirectResponse("/", status_code=303)

async def atualizar_tarefa(request:Request, tarefa_id:int, tarefa: str = Form(...)):
    tables.atualizar_tarefa(tarefa_id, tarefa)
    return RedirectResponse("/", status_code=303)

async def atualizar_status(request:Request, tarefa_id:int, status: bool = Form(False)):
    status_int = 1 if status else 0
    tables.atualizar_status(tarefa_id, status_int)
    return RedirectResponse("/", status_code=303)
