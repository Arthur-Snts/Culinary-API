from pydantic import BaseModel
from typing import List, Optional
from datetime import date


class Comentario(BaseModel):
    id: int
    texto: str
    data: date
    usuario_id: int
    receita_id: int


class Avaliacao(BaseModel):
    id: int
    nota: float
    comentario: Optional[str] = None
    usuario_id: int
    receita_id: int  


class Favorito(BaseModel):
    id: int
    usuario_id: int
    receita_id: int

class Receita(BaseModel):
    id: int
    nome: str
    descricao: str
    ingredientes: str
    modo_preparo: str
    usuario_id: int

    comentarios: List[Comentario] = []
    avaliacoes: List[Avaliacao] = []
    favoritos: List[Favorito] = []

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

    receitas: List[Receita] = []
    comentarios: List[Comentario] = []
    avaliacoes: List[Avaliacao] = []
    favoritos: List[Favorito] = []
