from fastapi import APIRouter #Roteador agrupa rotas/endpoints em um arquivo separado, dps e conectado na main com include_router
from fastapi import Depends #permite passar uma funcao como parametro para uma rota (usado nas sessions)
from fastapi import HTTPException #permite dar diferentes respostas de erro ao usuario, sem ele sempre retornaria codigo 200, que e o codigo que deu certo a requisicao
from models import Usuario, db 
from sqlalchemy.orm import Session 
from dependencies import pegar_sessao #importa a funcao pegar_sessao do arquivo dependencies
from main import bcrypt_context #usar o bcrypt_context declarado na main para criptografar a senha
from schemas import UsuarioSchema, LoginSchema #usando schemas para os dados nao serem enviados no URL mas sim como JSON dentro da rota


auth_router = APIRouter(prefix="/auth", tags=["Rotas de Autenticacao"]) #tudo de autenticacao vai estar no prefixo dominio/auth, a tag é o nome que vai estar no /docs

@auth_router.get("/")
async def home():
    """
    Essa e a rota padrão de autenticação
    """
    return {"mensagem": "Voce acessou a rota padrao de autenticacao"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):  #Para criar uma conta a rota post exige um nome,e-mail e senha que estao no UsuarioSchema>schemas.py e usa a pegar_sessao
#declarada no arquivo dependencies.py para conseguir acessar o banco dados. Uma boa prática e passar para função o (parametro: tipo_de_dado, parametro: tipo_de_dado)
#ao invés de usar varios parametros, é criado uma classe(Schema) que tem todos os parametros dentro dele

#async def criar_conta(email: str, senha: str, nome: str, session=Depends(pegar_sessao)): ----sem schema    
    
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first() #consulta a tabela usuario na coluna email usando a session que esta conectada com o banco e verifica
    #se o email passado como parametro ja esta no banco
    #Depends(pegar_sessao), recebe a funcao "pegar_sessao" do arquivo dependencies.py como parametro para nao ter que ficar escrevendo toda hora
    #o depends serve para passar a funcao como parametro e passar seu retorno
    
    if usuario: 
        #ja achou um usuario cadastrado com o mesmo email
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado!") #mensagem de erro ao usuario, usa raise ao inves de return para retornar o erro 400 e nao o codigo 200
    else:
        #nao achou nenhum email igual ao que o usuario passou, entao efetivamente cria o usuario

        senha_criptografada = bcrypt_context.hash(usuario_schema.senha) #criando a hash com a senha do usuario importando o bcrypt_context declarado no arquivo main

        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)

        session.add(novo_usuario) #adiciona o novo usuário, mas ainda nao commita para o banco
        session.commit() #sobe o novo usuario para o banco

        return {"Mensagem": f"Usuário cadastrado com sucesso {usuario_schema.email}"} 

#login -> email e senha -> gera JWT token -> JWT(JSON Web Token) token é utilizado para acessar outras rotas.
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)): #para realizar o login tem que receber a sessão do banco + email e senha do schema login
    
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first() #verifica se o email que o usuario inseriu existe no banco

    if usuario:
        ...
    


    






