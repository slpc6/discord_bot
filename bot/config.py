"""Archivo  para cargar las variables de entorno y configuraciones del bot"""

#External libraries
import os
from dotenv import load_dotenv


load_dotenv()


class config:
    
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    PREFIX = os.getenv("PREFIX")
    API_KEY =  os.getenv("OPENAI_API_KEY")
