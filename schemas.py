# O arquivo schemas.py é criado com o objetivo de passar para as rotas um modelo de parâmetros pre-definidos
#Isso faz com que:
# Os dados sejam validados previamente antes de entrar em uma rota POST (Verifica se oq o usuário digitou é tipo correto da variável) e se nao for retorna o erro 422 automaticamente
# Os parametros nao entrem na URL da rota (queryparameters) (http://127.0.0.1:8000/auth/criar_conta?email=tonicioli50%40gmail.com&senha=123&nome=jonatas), 
# mas sim no corpo da requisicao (JSON) 

from pydantic import BaseModel 
from typing import Optional

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    # class Config:
    #     from_attributes = True

class PedidoSchema(BaseModel): #pedido nao recebe nem id nem status nem valor nem preço, apenas o usuario.
    id_usuario: int #foreign key da tabela usuario
    