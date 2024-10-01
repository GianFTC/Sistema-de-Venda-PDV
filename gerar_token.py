import requests

login_url = 'http://127.0.0.1:5000/login'
login_data = {
    'username': 'User',  # Substitua pelo seu nome de usuário
    'password': '1010'     # Substitua pela sua senha
}

response = requests.post(login_url, json=login_data)
token = response.json().get('access_token')
print("Novo Token:", token)
