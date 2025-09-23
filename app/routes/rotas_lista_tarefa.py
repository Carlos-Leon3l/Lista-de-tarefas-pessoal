from fastapi import APIRouter, Request, Depends
from controllers import lista_tarefas_controller
from security.token import get_current_user
from models.user_model import TokenPayload


router = APIRouter()

@router.get("/")
def pagina_inicial(request: Request, require_permission: TokenPayload = Depends(get_current_user)):
    return lista_tarefas_controller.mostrar_tarefa(request, require_permission)

@router.post("/adicionar_tarefa")
async def adicionar(request:Request,  require_permission: TokenPayload = Depends(get_current_user)):
    form = await request.form()
    return await lista_tarefas_controller.adicionar_tarefa(request, require_permission, tarefa=form["tarefa"])

@router.get("/tarefa/delete/{tarefa_id}")
def deletar(tarefa_id: int):
    return lista_tarefas_controller.excluir_tarefa(tarefa_id)

@router.get("/tarefa/edit/{tarefa_id}")
def editar_tarefa(request:Request, tarefa_id:int):
    return lista_tarefas_controller.mostrar_edicao(request,tarefa_id)

@router.post("/tarefa/update/{tarefa_id}")
async def atualizar(request:Request, tarefa_id:int):
    form = await request.form()
    return await lista_tarefas_controller.atualizar_tarefa(request,tarefa_id, tarefa=form["tarefa"])


@router.post("/tarefa/update_status/{tarefa_id}")
async def atualizacao_status(request:Request, tarefa_id:int):
    form = await request.form()
    status = 1 if form.get("status") == "on" else 0
    print(status)
    return await lista_tarefas_controller.atualizar_status(request,tarefa_id, status)
    
    
