#o arquivo dependencis é criado com o objetivo de criar funções para serem passadas como parametros para as rotas da API
#deixando o código mais limpo, por meio do Depends()

from models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session # fábrica de sessões, usadas pra adicionar, buscar e salvar dados no banco
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM, oauth2_schema



def pegar_sessao(): #funcao criada criar a conexão com o banco e gerar uma sessao  nele
     try: #tente criar a session
          Session = sessionmaker(bind=db) #gera uma fabrica de sessões, conectada com o banco
          session = Session() #gera o objeto que sera usado para gerar consulta
          
          yield session #yeald é tipo um return mas que nao encerra a funcao, permitindo dar comandos apos ele

     finally: #se deu erro ou nao a session sempre vai ser fechada, o finally é executado se tiver erro ou noa
          session.close() #fechar sessao

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)): #verifica se o token passado é valido, se for válido retorna o usuário id 
#o token é passado com o auth2_schema para ser passado como header da requisição e nao como query
    
    try:
     dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM) #pega o jwt code enviado e retorna um dicionario  
     '''
               {
               "sub": "1",
               "exp": "1793651601",
               }
     '''
     id_usuario = dic_info.get("sub") #pegando o "sub" do dicionario gerado, o sub é o id do usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado verifique a validade do TOKEN")
        
    
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first() #pega o objeto usuario usando o id_usuario extraido do JWT token
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido esse usuário não existe") #o banco nao retornou nenhum objeto com o id_usuario extraido do JWT
    return usuario