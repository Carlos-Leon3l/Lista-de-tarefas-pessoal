from database.db import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" SELECT table_name 
                   FROM user_tables
                   WHERE table_name = 'USUARIOS'
                   """)
    if not cursor.fetchone():
        print("Iniciando a PRIMEIRA ligacao de TABELA")
        cursor.execute(""" 
        CREATE TABLE usuarios (
        id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        username VARCHAR2(255) NOT NULL, 
        email VARCHAR2(255) NOT NULL,
        password VARCHAR2(255) NOT NULL,
        data_criacao TIMESTAMP DEFAULT SYSTIMESTAMP
    )
    """)
    else:
        print("tabela usuarios já existe") 
        
    print("Criando tabela lista_tarefas")
    cursor.execute(""" SELECT table_name 
                   FROM user_tables
                   WHERE table_name = 'LISTA_TAREFAS'
                   """)
    if not cursor.fetchone():
        cursor.execute("""
    CREATE TABLE lista_tarefas (
        id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        tarefa VARCHAR2(255) NOT NULL, 
        status NUMBER(1) DEFAULT 0,
        usuario_id NUMBER,
        CONSTRAINT fk_usuario_tarefa
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )                
    """)
    else:
        print("tabela lista_tarefas já existe")    
    conn.commit()
    conn.close()
    
def inserir_tarefa(usuario_id, tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lista_tarefas (tarefa) VALUES (:1) WHERE usuario_id = :2", [tarefa, usuario_id])
    conn.close()
    
def listar_tarefas(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_tarefas WHERE usuario_id = :1", [usuario_id])
    tarefas = cursor.fetchall()
    conn.commit() 
    conn.close()
    return tarefas

def excluir_tarefa(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lista_tarefas WHERE id = :1", [tarefa_id])
    conn.commit()
    conn.close()
    
def buscar_tarefa_por_id(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lista_tarefas WHERE id = :1", [tarefa_id])
    tarefa = cursor.fetchone()
    conn.close()
    conn.commit()
    return tarefa

def atualizar_tarefa(tarefa_id, tarefa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""UPDATE lista_tarefas 
                   SET tarefa = :1
                   WHERE id = :2
                   """, [tarefa, tarefa_id])
    conn.commit()
    conn.close()

def atualizar_status(tarefa_id, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(""" UPDATE lista_tarefas
                   SET status = :1
                   WHERE id = :2 
                   """, [status, tarefa_id])
    conn.commit()
    conn.close()
    
def create_user(username, email, password):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO usuarios 
                   (username, email, password) VALUES (:1, :2, :3)
                   """, [username, email, password])
    conn.commit()
    conn.close()
    
def get_user_by_id(usuario_id:int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email, password FROM usuarios WHERE id = :1", [usuario_id])
    todos_dados_usuarios = cursor.fetchone()
    if todos_dados_usuarios:
        user_dict = {
            "id": todos_dados_usuarios[0],
            "username": todos_dados_usuarios[1],
            "email": todos_dados_usuarios[2],
            "password": todos_dados_usuarios[3]
        }
        return user_dict
    conn.commit()
    conn.close()
    
def get_user_by_email(email:str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT id, email, password FROM usuarios WHERE email = :1
                   """, [email])
    retorno_email = cursor.fetchone()
    if retorno_email:
        user_dict = {
        "id": retorno_email[0], #ERREI A DISGRACA DO NOME KKKKKKKKKKKK
        "email": retorno_email[1],
        "password": retorno_email[2]
        }
        return user_dict
    conn.commit()
    conn.close()
    
