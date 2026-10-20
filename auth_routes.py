from fastapi import APIRouter, Depends #Roteador agrupa rotas/endpoints em um arquivo separado, dps e conectado na main com include_router
from models import Usuario, db 
# from sqlalchemy.orm import sessionmaker 
from dependencies import pegar_sessao #importa a funcao pegar_sessao do arquivo dependencies


auth_router = APIRouter(prefix="/auth", tags=["Rotas de Autenticacao"]) #tudo de autenticacao vai estar no prefixo dominio/auth, a tag é o nome que vai estar no /docs

@auth_router.get("/")
async def home():
    """
    Essa e a rota padrão de autenticação
    """
    return{"mensagem": "Você acessou a rota padrão de autenticação","autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)): #colocar str faz o FastAPI fazer a validação se oq usuário passar é string (O Fast já faz o tratamento)
    
    usuario = pegar_sessao.query(Usuario).filter(Usuario.email == email).first() #consulta a tabela usuario na coluna email usando a session que esta conectada com o banco e verifica
    #se o email passado como parametro ja esta no banco
    #Depends(pegar_sessao), recebe a funcao "pegar_sessao" do arquivo dependencies.py como parametro para nao ter que ficar escrevendo toda hora
    #o depends serve para passar a funcao como parametro e passar seu retorno
    
    if usuario: 
        #ja achou um usuario cadastrado com o mesmo email
        return{"Mensagem": "Já existe um usuário com esse email"}
    else:
        #nao achou nenhum email igual ao que o usuario passou, entao efetivamente cria o usuario
        novo_usuario = Usuario(nome, email, senha)
        pegar_sessao.add(novo_usuario) #adiciona o novo usuário, mas ainda nao commita para o banco
        pegar_sessao.commit() #sobe o novo usuario para o banco
        return {"Mensagem": "Usuário cadastrado com sucesso"} 


    






