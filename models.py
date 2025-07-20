from sqlmodel import SQLModel, Field
from typing import List
from datetime import date


class Comentario(SQLModel, table = True):
    id: int = Field(primary_key=True)
    texto: str = Field(index=False)
    data: date = Field(index=False)
    usuario_id: int = Field()
    receita_id: int = Field()


class Avaliacao(SQLModel, table = True):
    id: int = Field(primary_key=True)
    nota: float = Field(index=False)
    comentario:str | None = Field(index=False, default=None)
    usuario_id: int = Field()
    receita_id: int  = Field()


class Favorito(SQLModel, table = True):
    id: int = Field(primary_key=True)
    usuario_id: int = Field()
    receita_id: int = Field()

class Receita(SQLModel, table = True):
    id: int = Field(primary_key=True)
    nome: str = Field(index=False)
    descricao: str = Field(index=False)
    ingredientes: str = Field(index=False)
    modo_preparo: str = Field(index=False)
    usuario_id: int = Field()

    

class Usuario(SQLModel, table = True):
    id: int  = Field(primary_key=True)
    nome: str = Field(index=False)
    email: str= Field(index=False)
    senha: str = Field(index=False)

    