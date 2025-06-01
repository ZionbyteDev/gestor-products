import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('DB_HOST', '127.0.0.1'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'gestor_productos')
        )
        return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None 
    
