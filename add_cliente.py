import requests

# Função para obter o token JWT
def get_jwt_token(login_url, login_data):
    response = requests.post(login_url, json=login_data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print('Falha ao gerar token. Verifique as credenciais.')
        print('Status Code:', response.status_code)
        print('Response:', response.text)
        return None

# Função para adicionar um cliente usando o token JWT
def add_client(url, token, data):
    headers = {
        'Authorization': f'Bearer {token}',  # Use o token JWT gerado
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=data, headers=headers)
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Resposta não está em formato JSON:")
        print(response.text)

# URLs e dados
login_url = 'http://127.0.0.1:5000/login'
login_data = {
    'username': 'User',  # Substitua pelo nome de usuário correto
    'password': '1010'   # Substitua pela senha correta
}

clients_url = 'http://127.0.0.1:5000/clients'
client_data = {
    'name': input('Nome do Cliente:'),
    'email': input('Email do Cliente:'),
    'phone': input('tel :'),
}

# Executa o fluxo
token = get_jwt_token(login_url, login_data)
if token:
    add_client(clients_url, token, client_data)
