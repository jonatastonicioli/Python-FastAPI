from fastapi import FastAPI #importando o fastAPI
from passlib.context import CryptContext #biblioteca de criptografia de senhas
from dotenv import load_dotenv

minha_api = FastAPI() #criando o objeto/instancia minha_api coma classe FastAPI, sem nenhum parametro

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