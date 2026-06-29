import os
from dotenv import load_dotenv 

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    
    # Escribe tus datos de MySQL directamente aquí (reemplaza con tu contraseña y base real)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://eshop_user:EshopPass2026@localhost/eshop_db'