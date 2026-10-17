from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["Rotas de Pedidos"])

@order_router.get("/") #para criar uma rota vai usar o roteador + indicar o tipo de requisicao get/post/put/delete + o novo caminho + criar uma funcao
#nesse caso o caminho é dominio.com/pedidos 
async def pedidos():
    """
    Essa e a rota padrão de pedidos. Todas as rotas dos pedidos precisam de autenticação
    """
    return {"mensagem": "Você acessou a rota pedidos"} #dicionario