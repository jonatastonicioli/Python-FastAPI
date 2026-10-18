from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Boolean, Integer, Float, ForeignKey #importando tipos de dados que serão utilizados nas colunas do banco
from sqlalchemy_utils import ChoiceType #permite que a coluna status da tabela pedido apenas possa receber "Pendente","Cancelado" e "Finalizado" (tupla de tuplas ) e nada mais


#SQLalchemy ORM
#criando conexão do banco python com sqlite
db = create_engine("sqlite:///banco.db") # "sqlite:///banco.db" = tipo do banco (sqlite) + arquivo onde os dados ficam (banco.db), db é uma instância/objeto

#Cria a classe base onde todas os modelos (tabelas) vão herdar, O declarative_base() é uma função que fabrica uma classe.
#É essa base que faz o python entender que a classes que que recebem como parametro essa base são tabelas e nao classes simples
Base = declarative_base() 

#Criar as clases que serão as tabelas do banco Usuario,Pedidos,ItensPedidos

class Usuario(Base):
    __tablename__ = "usuarios" #define o nome da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True) #a coluna do meu banco vai ter o nome id, e eu acesso no python essa coluna a partir da variavel id
    nome = Column("nome", String)
    email = Column("email", String, nullable=False) #nao aceita valor vazio
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)    #o padrão da admin é false, so será true se receber um parametro true

    def __init__(self, nome, email, senha, ativo=True, admin=False): #função construtora usada para criar novos usuarios ao longo do codigo python, sem id pq o id e criado sozinho
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# STATUS_PEDIDOS = ( #Exige que a coluna status da tabela Pedido só possa receber esses valores
#     #(chave,valor) chave =oq e armazenado no bando, valor= oq aparace qnd vc printa a chave, poderia ser ("P", "Pendente"),
#     ("PENDENTE","PENDENTE"),
#     ("CANCELADO","CANCELADO"),
#     ("FINALIZADO","FINALIZADO"),
# ) #tupla de tuplas 

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # status= Column("status", ChoiceType(choices=STATUS_PEDIDOS) ) #Pendente, Cancelado, Finalizado
    status= Column("status", String) #Pendente, Cancelado, Finalizado
    usuario= Column ("usuario", ForeignKey("usuarios.id")) #a coluna usuario da tabela pedido é uma chave estrangeira da tabela usuario, e elas são relacionadas pelo id do usuario
    preco= Column("preco", Float)
    #itens=Column("itens", )

    def __init__(self,  usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco

class ItensPedido (Base):
    __tablename__ = "itens_pedido"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade= Column("quantidade", Integer, nullable=False)
    sabor= Column("sabor", String)
    tamanho= Column("tamanho", String)
    preco_unitario= Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, quantidade,sabor,tamanho,preco_unitario):
        self.quantidade = quantidade
        self.sabor= sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario



