from fastapi import FastAPI #importando o fastAPI
from passlib.context import CryptContext #biblioteca de criptografia de senhas
from dotenv import load_dotenv #conseguir ler o arquivo .env para trazer a secret_key usada para criptografar
import os 

load_dotenv() #lê o .env e carrega as variáveis

SECRET_KEY = os.getenv("SECRET_KEY") #procura no arquivo .env a secret_key e retorna para variavel o valor encontrado, uso no JWT token

minha_api = FastAPI() #criando o objeto/instancia minha_api coma classe FastAPI, sem nenhum parametro

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #gera o objeto que é capaz de gerar o hash da senha (usa nas auth_routes)

from auth_routes import auth_router #importar as rotas dps de ter criado o objeto
from order_routes import order_router

minha_api.include_router(auth_router)
minha_api.include_router(order_router)


#uvicorn main:minha_api --reload o servidor uvicorn executa a variavel/objeto "minha_api(FastAPI)" que esta no arquivo main.py, o reload faz com que cada alteração
# no codigo ja suba para o servidor automaticamente





#endpoint/rota
#teste.com/ordens 
#/ordens (path)

'''
Requisições:
GET - Leitura/Pegar
POST - Enviar
PUT - Edição
DELETE - Deletar
'''