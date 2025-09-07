from dotenv import load_dotenv
import oracledb
import os
load_dotenv()
 
def conectar():
    oracledb.init_oracle_client()

    conn = oracledb.connect(
    user= os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn = os.getenv("ORACLE_DSN")
    )
    print("conectado")
    return conn
 