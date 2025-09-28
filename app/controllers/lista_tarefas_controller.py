from fastapi import Request, Form, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import tables
from models.user_model import TokenPayload
from security.token import get_current_user

tables.criar_tabela()

def mostrar_tarefa(current_user_by_id: TokenPayload):
    tarefas = tables.listar_tarefas(current_user_by_id.usuario_id)
    return tarefas 

# def mostrar_edicao(request:Request , tarefa_id:int):
#     tarefa = tables.buscar_tarefa_por_id(tarefa_id)
#     tarefas = tables.listar_tarefas()
#     return templates.TemplateResponse("Listagem/editar.html", {
#         "request": request, "tarefa":tarefa, "tarefas":tarefas}
#         )

def adicionar_tarefa(tarefa:str,current_user_by_id:TokenPayload): 
    return tables.inserir_tarefa(tarefa,current_user_by_id.usuario_id)

def excluir_tarefa(tarefa_id:int, current_user_by_id:TokenPayload):
    return tables.repo_excluir_tarefa(tarefa_id, current_user_by_id.usuario_id)
    

async def atualizar_tarefa(tarefa_id:int, tarefa:str, current_user_by_id:TokenPayload):
    return tables.atualizar_tarefa(tarefa_id, tarefa, current_user_by_id.usuario_id)

async def atualizar_status(tarefa_id:int, current_user_by_id: TokenPayload):
    tarefa_by_id = tables.buscar_tarefa_por_id(tarefa_id)
    print("id da tarefa", tarefa_by_id)
    status_tarefa = tarefa_by_id.get('status')
    if status_tarefa == 0:
        status_tarefa = 1
    elif status_tarefa == 1:
        status_tarefa = 0
    
    print("status_pos_mudanca", status_tarefa)
    novo_status = status_tarefa
    print("novo_status", novo_status)
    
    return tables.repo_atualizar_status(novo_status,tarefa_id,current_user_by_id.usuario_id)
     



