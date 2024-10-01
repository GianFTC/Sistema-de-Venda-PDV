import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/Thiago/Desktop/Sistema de venda PDV/backend/banco_de_dados/meu_banco_de_dados.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
