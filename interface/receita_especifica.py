import requests
from sessao import sessao
from datetime import datetime

URL = "http://127.0.0.1:8000"

def favoritar_receita():
    favorito = {
        "usuario_id": sessao.usuario_id,
        "receita_id": sessao.receita_id
    }
    r = requests.post(f"{URL}/Favoritos/", json=favorito)
    if r.status_code in (200, 201):
        print("Receita favoritada.")
    else:
        print(f"Erro ao favoritar: {r.status_code} - {r.text}")

def desfavoritar_receita():
    # Buscar favoritos do usuário para encontrar o id do favorito referente à receita
    r = requests.get(f"{URL}/Favoritos/", params={"usuario_id": sessao.usuario_id})
    if r.status_code != 200:
        print(f"Erro ao buscar favoritos: {r.text}")
        return

    favoritos = r.json()
    favorito_id = None
    for fav in favoritos:
        if fav["receita_id"] == sessao.receita_id:
            favorito_id = fav["id"]
            break

    if favorito_id is None:
        print("Receita não está favoritada.")
        return

    r = requests.delete(f"{URL}/Favoritos/", params={"favorito_id": favorito_id})
    if r.status_code == 200:
        print("Receita desfavoritada.")
    else:
        print(f"Erro ao desfavoritar: {r.status_code} - {r.text}")

def mostrar_media_avaliacao():
    r = requests.get(f"{URL}/Avaliacoes/", params={"receita_id": sessao.receita_id})
    if r.status_code != 200:
        print("Nenhuma avaliação encontrada para essa receita.")
        return

    avaliacoes = r.json()
    media = sum(av["nota"] for av in avaliacoes) / len(avaliacoes)
    print(f"Média das avaliações: {media:.2f} ({len(avaliacoes)} avaliações)")

def avaliar_receita():
    print(f"\n[sessao] Usuario ID: {sessao.usuario_id} | Receita ID: {sessao.receita_id}")

    # Verifica se já avaliou
    r = requests.get(f"{URL}/Avaliacoes/usuario-receita", params={
        "usuario_id": sessao.usuario_id,
        "receita_id": sessao.receita_id
    })

    if r.status_code == 200:
        avaliacao = r.json()
        print(f"Você já avaliou essa receita com nota {avaliacao['nota']}")
        alterar = input("Deseja alterar a avaliação? (s/n): ").lower()
        if alterar == 's':
            nota = int(input("Nova nota (1 a 5): "))
            nova_avaliacao = {
                "id": avaliacao["id"],  # precisa ter o ID da avaliação
                "usuario_id": sessao.usuario_id,
                "receita_id": sessao.receita_id,
                "nota": nota
            }
            r = requests.put(f"{URL}/Avaliacoes", json=nova_avaliacao)
            if r.status_code == 200:
                print("Avaliação atualizada.")
            else:
                print("Erro ao atualizar avaliação:", r.text)
        else:
            print(" Avaliação mantida.")
    else:
        print("Você ainda não avaliou essa receita.")
        nota = int(input("Digite uma nota de 1 a 5: "))
        nova_avaliacao = {
            "usuario_id": sessao.usuario_id,
            "receita_id": sessao.receita_id,
            "nota": nota
        }
        print(f"[DEBUG] Enviando avaliação: {nova_avaliacao}")
        r = requests.post(f"{URL}/Avaliacoes/", json=nova_avaliacao)
        if r.status_code in (200, 201):
            print("Avaliação criada.")
        else:
            print("Erro ao criar avaliação:", r.text)

def listar_comentarios():
    r = requests.get(f"{URL}/Comentarios/", params={"receita_id": sessao.receita_id})
    if r.status_code != 200:
        print("Nenhum comentário para essa receita.")
        return
    comentarios = r.json()
    print(f"Comentários ({len(comentarios)}):")
    for c in comentarios:
        print(f"- Usuário {c['usuario_id']}: {c['texto']}")

def criar_comentario():
    if sessao.receita_id is None or sessao.usuario_id is None:
        print("Receita ou usuário não selecionado.")
        return

    texto = input("Digite seu comentário: ").strip()
    if not texto:
        print("Comentário não pode ser vazio.")
        return

    comentario_cadastra = {
        "texto": texto,
        "usuario_id": sessao.usuario_id,
        "receita_id": sessao.receita_id
        # NÃO enviar campo 'data', backend insere a hora atual automaticamente
    }

    r = requests.post(f"{URL}/Comentarios/", json=comentario_cadastra)

    if r.status_code in (200, 201):
        print("Comentário criado com sucesso.")
    else:
        print(f"Erro ao criar comentário: {r.status_code} - {r.text}")


def atualizar_comentario():
    comentario_id = input("Digite o ID do comentário que deseja alterar: ")
    novo_texto = input("Digite o novo texto do comentário: ")
    comentario_atualiza = {
        "id": int(comentario_id),
        "texto": novo_texto,
        "data": datetime.now().isoformat(),  # atualiza para a data atual
        "usuario_id": sessao.usuario_id,
        "receita_id": sessao.receita_id
    }
    r = requests.put(f"{URL}/Comentarios/", json=comentario_atualiza)
    if r.status_code == 200:
        print("Comentário atualizado com sucesso.")
    else:
        print(f"Erro ao atualizar comentário: {r.status_code} - {r.text}")


def deletar_comentario():
    # Busca o comentário do usuário para essa receita para pegar o id
    r = requests.get(f"{URL}/Comentarios/usuario-receita", params={"usuario_id": sessao.usuario_id, "receita_id": sessao.receita_id})
    if r.status_code != 200:
        print("Você não possui comentário para deletar.")
        return
    comentario = r.json()
    r = requests.delete(f"{URL}/Comentarios/", params={"comentario_id": comentario["id"]})
    if r.status_code == 200:
        print("Comentário deletado.")
    else:
        print("Erro ao deletar comentário:", r.text)

def menu_receita_especifica():
    while True:
        print(f"\n=== Receita ID {sessao.receita_id} ===")
        print("1. Favoritar")
        print("2. Desfavoritar")
        print("3. Avaliar / Alterar avaliação")
        print("4. Mostrar média das avaliações")
        print("5. Comentar (criar comentário)")
        print("6. Editar comentário existente")
        print("7. Deletar comentário")
        print("8. Listar todos os comentários")
        print("0. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            favoritar_receita()
        elif opcao == "2":
            desfavoritar_receita()
        elif opcao == "3":
            avaliar_receita()
        elif opcao == "4":
            mostrar_media_avaliacao()
        elif opcao == "5":
            criar_comentario()       # função para criar comentário (nova)
        elif opcao == "6":
            atualizar_comentario()      # função para editar comentário (nova)
        elif opcao == "7":
            deletar_comentario()
        elif opcao == "8":
            listar_comentarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

