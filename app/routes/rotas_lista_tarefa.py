from fastapi import APIRouter, Request, Depends, HTTPException
from controllers import lista_tarefas_controller
from security.token import get_current_user
from models.user_model import TokenPayload


router = APIRouter()

@router.get("/", status_code=200)
def pagina_inicial(require_permission: TokenPayload = Depends(get_current_user)):
    return lista_tarefas_controller.mostrar_tarefa(require_permission)

@router.post("/adicionar_tarefa", status_code=201)
def adicionar(nome_tarefa:str, require_permission: TokenPayload = Depends(get_current_user)):
    lista_tarefas_controller.adicionar_tarefa(nome_tarefa, require_permission)
    
    return {"tarefa criada":{
        "nome da tarefa": nome_tarefa,
        "usuario_id": require_permission
    }}

@router.delete("/tarefa/delete/{tarefa_id}", status_code=303)
def deletar_tarefa(tarefa_id: int, require_permission: TokenPayload = Depends(get_current_user)):
    lista_tarefas_controller.excluir_tarefa(tarefa_id, require_permission)
    return {"Tarefa excluida com exito"}

#@router.get("/tarefa/edit/{tarefa_id}")
#def editar_tarefa(request:Request, tarefa_id:int):
#    return lista_tarefas_controller.mostrar_edicao(request,tarefa_id)

@router.put("/tarefa/update/{tarefa_id}", status_code=303)
async def atualizar(tarefa_id:int, tarefa, require_permission: TokenPayload = Depends(get_current_user)):
    await lista_tarefas_controller.atualizar_tarefa(tarefa_id, tarefa,require_permission)
    return ["Tarefa atualizada com exito",{
        "tarefa_id": tarefa_id,
        "tarefa": tarefa
    }]

@router.put("/tarefa/update_status/{tarefa_id}", status_code=303)
async def atualizacao_status(tarefa_id:int, require_permission: TokenPayload = Depends(get_current_user)):
    await lista_tarefas_controller.atualizar_status(tarefa_id,require_permission)
    return ["status modificado com exito", {
        "tarefa": tarefa_id
    }]