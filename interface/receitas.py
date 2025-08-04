import requests
from sessao import sessao
from receita_especifica import menu_receita_especifica

URL = "http://127.0.0.1:8000"

def listar_receitas():
    try:
        resposta = requests.get(f"{URL}/Receitas/")
        if resposta.status_code == 200:
            receitas = resposta.json()
            if not receitas:
                print("\nNenhuma receita cadastrada.")
            else:
                print("\n=== TODAS AS RECEITAS ===")
                for r in receitas:
                    print(f"\nID: {r['id']}")
                    print(f"Nome: {r['nome']}")
                    print(f"Descrição: {r['descricao']}")
                    print(f"Ingredientes: {r['ingredientes']}")
                    print(f"Modo de Preparo: {r['modo_preparo']}")
                    print(f"Autor (usuário_id): {r['usuario_id']}")
        else:
            print(f"Erro ao listar receitas: {resposta.status_code}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def criar_receita():
    print("\n=== CRIAR NOVA RECEITA ===")
    nome = input("Nome: ").strip()
    descricao = input("Descrição: ").strip()
    ingredientes = input("Ingredientes: ").strip()
    modo_preparo = input("Modo de preparo: ").strip()

    if not all([nome, descricao, ingredientes, modo_preparo]):
        print("Todos os campos são obrigatórios.")
        return

    dados = {
        "nome": nome,
        "descricao": descricao,
        "ingredientes": ingredientes,
        "modo_preparo": modo_preparo,
        "usuario_id": sessao.usuario_id
    }

    try:
        resposta = requests.post(f"{URL}/Receitas/", json=dados)
        if resposta.status_code in (200, 201):
            print(" Receita criada com sucesso!")
        else:
            print(f"Erro ao criar receita: {resposta.status_code} - {resposta.text}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def entrar_receita():
    receita_id = input("Digite o ID da receita que deseja acessar: ").strip()
    if not receita_id.isdigit():
        print("ID inválido.")
        return

    sessao.receita_id = int(receita_id)
    menu_receita_especifica()

def ver_favoritos():
    try:
        resposta = requests.get(f"{URL}/Favoritos/", params={"usuario_id": sessao.usuario_id})
        if resposta.status_code == 200:
            favoritos = resposta.json()
            if not favoritos:
                print("\nNenhuma receita favorita encontrada.")
            else:
                print("\n=== SUAS RECEITAS FAVORITAS ===")
                for fav in favoritos:
                    print(f"ID Favorito: {fav['id']}, Receita ID: {fav['receita_id']}, Usuário ID: {fav['usuario_id']}")
        else:
            print(f"Erro ao buscar favoritos: {resposta.status_code} - {resposta.text}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    

def menu_receitas():
    while True:
        print(f"\n=== MENU DE RECEITAS (Usuário ID: {sessao.usuario_id}) ===")
        print("1. Listar todas as receitas")
        print("2. Criar nova receita")
        print("3. Ver receitas favoritas")
        print("4. Entrar em uma receita específica")
        print("0. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar_receitas()
        elif opcao == "2":
            criar_receita()
        elif opcao == "3":
            ver_favoritos()
        elif opcao == "4":
            entrar_receita()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
