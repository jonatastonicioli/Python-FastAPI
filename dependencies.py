#o arquivo dependencis é criado com o objetivo de criar funções para serem passadas como parametros para as rotas da API
#deixando o código mais limpo, por meio do Depends()

from models import db
from sqlalchemy.orm import sessionmaker # fábrica de sessões, usadas pra adicionar, buscar e salvar dados no banco

def pegar_sessao(): #funcao criada criar a conexão com o banco e gerar uma sessao  nele
     try: #tente criar a session
          Session = sessionmaker(bind=db) #gera uma fabrica de sessões, conectada com o banco
          session = Session() #gera o objeto que sera usado para gerar consulta
          
          yield session #yeald é tipo um return mas que nao encerra a funcao, permitindo dar comandos apos ele

     finally: #se deu erro ou nao a session sempre vai ser fechada, o finally é executado se tiver erro ou noa
          session.close() #fechar sessao