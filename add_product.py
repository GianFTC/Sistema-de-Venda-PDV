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

# Função para adicionar um produto usando o token JWT
def add_product(url, token, data):
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

product_url = 'http://127.0.0.1:5000/products'
product_data = {
    'name': input('Nome do Produto: '),
    'price': float(input('Valor: ')),  # Use float() para valores decimais
    'stock': int(input('Quantidade: '))
}

# Executa o fluxo
token = get_jwt_token(login_url, login_data)
if token:
    add_product(product_url, token, product_data)
