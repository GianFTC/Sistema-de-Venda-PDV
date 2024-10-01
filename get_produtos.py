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

# Função para consultar os produtos usando o token JWT
def get_products(url, token):
    headers = {
        'Authorization': f'Bearer {token}',  # Use o token JWT gerado
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    try:
        products = response.json()
        print(products)
    except requests.exceptions.JSONDecodeError:
        print("Resposta não está em formato JSON:")
        print(response.text)

# URLs e dados
login_url = 'http://127.0.0.1:5000/login'
login_data = {
    'username': 'User',  
    'password': '1010'   
}

product_url = 'http://127.0.0.1:5000/products'

# Executa o fluxo
token = get_jwt_token(login_url, login_data)
if token:
    get_products(product_url, token)
