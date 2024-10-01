import requests
from requests.auth import HTTPBasicAuth

def configure_router(ip, port, username, password):
    try:
        # Exemplo de URL e payload para um roteador com suporte a API
        url = f"http://{ip}/api/port-forwarding"
        payload = {
            "port": port,
            "protocol": "TCP",
            "internal_ip": "192.168.0.6",
            "internal_port": port,
            "enabled": True
        }
        response = requests.post(url, json=payload, auth=HTTPBasicAuth(username, password))
        
        if response.status_code == 200:
            print(f"Redirecionamento de portas configurado com sucesso.")
        else:
            print(f"Erro ao configurar o redirecionamento de portas: {response.text}")
    except requests.RequestException as e:
        print(f"Erro ao configurar o roteador: {e}")

if __name__ == "__main__":
    router_ip = "192.168.0.1"  # IP do seu roteador
    router_port = 5000         # Porta a ser redirecionada
    router_username = "Fox"  # Nome de usuário do roteador
    router_password = "carro2323"  # Senha do roteador
    configure_router(router_ip, router_port, router_username, router_password)
