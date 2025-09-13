from fastapi import APIRouter, Request, Depends
from controllers import lista_tarefas_controller


router = APIRouter()


@router.get("/")
def pagina_inicial(request: Request):
    return lista_tarefas_controller.mostrar_tarefa(request)

@router.post("/tarefa")
async def adicionar(request:Request):
    form = await request.form()
    return await lista_tarefas_controller.adicionar_tarefa(request, tarefa=form["tarefa"])

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
    