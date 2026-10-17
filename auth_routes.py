from fastapi import APIRouter #Roteador agrupa rotas/endpoints em um arquivo separado, dps e conectado na main com include_router

auth_router = APIRouter(prefix="/auth", tags=["Rotas de Autenticacao"]) #tudo de autenticacao vai estar no prefixo dominio/auth, a tag é o nome que vai estar no /docs

@auth_router.get("/")
async def autenticar():
    """
    Essa e a rota padrão de autenticação
    """
    return{"mensagem": "Você acessou a rota padrão de autenticação","autenticado": False}


