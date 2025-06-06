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

## 4. /Avaliacoes

| Método | Endpoint            | Descrição                                          |
|--------|---------------------|----------------------------------------------------|
| GET    | /Avaliacoes/{nome_receita} | Mostra a avaliação de uma receita pesquisada pelo nome |
| GET    | /Avaliacoes            | Mostra a avaliação das receitas                      |
| POST   | /Avaliacoes            | Cadastra avaliação de uma receita                    |
| DELETE | /Avaliacoes            | Deletar avaliação de uma receita                      |
| PUT    | /Avaliacoes            | Alterar a avaliação de uma receita                    |

---

## 5. /Comentarios

| Método | Endpoint            | Descrição                                         |
|--------|---------------------|---------------------------------------------------|
| GET    | /Comentarios/{nome_receita} | Mostra os comentários de uma receita            |
| GET    | /Comentarios           | Mostra todos os comentários                        |
| POST   | /Comentarios           | Cadastra comentários de uma receita                |
| DELETE | /Comentarios           | Deletar um comentário de uma receita               |
| PUT    | /Comentarios           | Altera um comentário                                |

---

## 6. /Favoritos

| Método | Endpoint   | Descrição                          |
|--------|------------|----------------------------------|
| GET    | /Favoritos | Mostra todas as receitas favoritados |
| POST   | /Favoritos | Cadastra uma receita como favorito  |
| DELETE | /Favoritos | Remove uma receita dos favoritos    |
