from fastapi import APIRouter
from fastapi import Depends #antes de processar essa rota me de o retorno dessa funcao como paremetro!
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido



order_router = APIRouter(prefix="/pedidos", tags=["Rotas de Pedidos"])

@order_router.get("/") #para criar uma rota vai usar o roteador + indicar o tipo de requisicao get/post/put/delete + o novo caminho + criar uma funcao
#nesse caso o caminho é dominio.com/pedidos 
async def pedidos():
    """
    Essa e a rota padrão de pedidos. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota pedidos"} #dicionario

@order_router.post("/pedido")
async def criar_pedido(schema_pedido: PedidoSchema, session: Session = Depends(pegar_sessao)):

    novo_pedido = Pedido(usuario = schema_pedido.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return{"mensagem": f"Seu pedido foi criado com sucesso. ID do Pedido: {novo_pedido.id}"}



 