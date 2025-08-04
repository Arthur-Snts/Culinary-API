import requests
from sessao import sessao


BASE_URL = "http://127.0.0.1:8000"

def login():
    print("=== Login ===")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    # Chama a API passando email e senha na query string
    params = {"usu_email": email, "usu_senha": senha}
    r = requests.get(f"{BASE_URL}/Usuarios", params=params)

    if r.status_code == 200:
        data = r.json()
        # Se a resposta for um dict com mensagem de erro:
        if isinstance(data, dict) and "mensagem" in data:
            print(data["mensagem"])
            return False
        # Se for usuário válido, salva id na sessão:
        sessao.usuario_id = data["id"]
        print(f"\nBem-vindo, {data['nome']}!")
        return True
    else:
        print("Erro ao conectar com a API.")
        return False


def criar_conta():
    print("=== Criar Conta ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    r = requests.post(f"{BASE_URL}/Usuarios", json=usuario)
    if r.status_code in (200, 201):
        print(" Conta criada com sucesso!")
    else:
        print(f" Erro ao criar conta: {r.status_code}")
