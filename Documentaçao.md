# Culinary-API  
**IFRN – Campus Caicó**  
**Alunos:** Arthur Alves dos Santos e Artur Dantas de Medeiros  

---

## 1. /Receitas

| Método | Endpoint         | Descrição                          |
|--------|------------------|----------------------------------|
| GET    | /Receitas/{nome} | Pesquisa receitas pelo nome       |
| GET    | /Receitas        | Mostra todas as receitas          |
| POST   | /Receitas        | Cadastrar suas receitas           |
| DELETE | /Receitas        | Deletar suas receitas             |
| PUT    | /Receitas        | Altera algo na sua receita cadastrada |

---

## 2. /Usuarios

| Método | Endpoint   | Descrição                    |
|--------|------------|------------------------------|
| POST   | /Usuarios  | Cadastra uma conta            |
| DELETE | /Usuarios  | Deletar uma conta             |
| PUT    | /Usuarios  | Alterar algum atributo da conta |

---

## 3. /Login

| Método | Endpoint | Descrição                 |
|--------|----------|---------------------------|
| POST   | /Login   | Retorna um token de login |

---

## 4. /Avaliar

| Método | Endpoint            | Descrição                                          |
|--------|---------------------|----------------------------------------------------|
| GET    | /Avaliar/{nome_receita} | Mostra a avaliação de uma receita pesquisada pelo nome |
| GET    | /Avaliar            | Mostra a avaliação das receitas                      |
| POST   | /Avaliar            | Cadastra avaliação de uma receita                    |
| DELETE | /Avaliar            | Deletar avaliação de uma receita                      |
| PUT    | /Avaliar            | Alterar a avaliação de uma receita                    |

---

## 5. /Comentar

| Método | Endpoint            | Descrição                                         |
|--------|---------------------|---------------------------------------------------|
| GET    | /Comentar/{nome_receita} | Mostra os comentários de uma receita            |
| GET    | /Comentar           | Mostra todos os comentários                        |
| POST   | /Comentar           | Cadastra comentários de uma receita                |
| DELETE | /Comentar           | Deletar um comentário de uma receita               |
| PUT    | /Comentar           | Altera um comentário                                |

---

## 6. /Favoritar

| Método | Endpoint   | Descrição                          |
|--------|------------|----------------------------------|
| GET    | /Favoritar | Mostra todas as receitas favoritados |
| POST   | /Favoritar | Cadastra uma receita como favorito  |
| DELETE | /Favoritar | Remove uma receita dos favoritos    |
