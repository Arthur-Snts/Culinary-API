from sessao import sessao
from logar import login, criar_conta
from receitas import menu_receitas

def menu_login():
    if sessao.usuario_id is not None:
        print(f"Usuário logado com ID {sessao.usuario_id}. Mostrando receitas...")
        menu_receitas()
        return

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Login")
        print("2. Criar Conta")
        print("0. Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            if login():
                menu_receitas()
                return
        elif opcao == "2":
            criar_conta()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_login()
