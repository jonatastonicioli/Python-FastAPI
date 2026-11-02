#arquivo criado para fazer requisições direto no python sem o /docs

import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1IiwiZXhwIjoxNzk0MjYxMTMxfQ.EzVOrnb3WPMKn_K6mCmufQyfrTrY7iqImUvaiQ9JwxI"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)

print(requisicao)
print(requisicao.json())

