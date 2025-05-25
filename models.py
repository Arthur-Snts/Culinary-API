from __future__ import annotations

from typing import Optional, List
from sqlalchemy import (
    String, Text, ForeignKey, Float, DateTime, func, Integer, UniqueConstraint
)
from sqlalchemy.orm import (
    relationship, declarative_base, Mapped, mapped_column
)

Base = declarative_base()

class Usuario(Base):
    """Tabela de usuários."""
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    receitas: Mapped[List[Receita]] = relationship(back_populates='autor', cascade='all, delete-orphan')
    comentarios: Mapped[List[Comentario]] = relationship(back_populates='usuario', cascade='all, delete-orphan')
    avaliacoes: Mapped[List[Avaliacao]] = relationship(back_populates='usuario', cascade='all, delete-orphan')
    favoritos: Mapped[List[Favorito]] = relationship(back_populates='usuario', cascade='all, delete-orphan')


class Receita(Base):
    """Tabela de receitas criadas pelos usuários."""
    __tablename__ = 'receitas'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    ingredientes: Mapped[str] = mapped_column(Text, nullable=False)
    modo_preparo: Mapped[str] = mapped_column(Text, nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable=False)

    autor: Mapped[Usuario] = relationship(back_populates='receitas')
    comentarios: Mapped[List[Comentario]] = relationship(back_populates='receita', cascade='all, delete-orphan')
    avaliacoes: Mapped[List[Avaliacao]] = relationship(back_populates='receita', cascade='all, delete-orphan')
    favoritos: Mapped[List[Favorito]] = relationship(back_populates='receita', cascade='all, delete-orphan')


class Comentario(Base):
    """Tabela de comentários feitos em receitas."""
    __tablename__ = 'comentarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(Text, nullable=False)
    data: Mapped[DateTime] = mapped_column(default=func.now())
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable=False)
    receita_id: Mapped[int] = mapped_column(ForeignKey('receitas.id'), nullable=False)

    usuario: Mapped[Usuario] = relationship(back_populates='comentarios')
    receita: Mapped[Receita] = relationship(back_populates='comentarios')


class Avaliacao(Base):
    """Tabela de avaliações feitas por usuários em receitas."""
    __tablename__ = 'avaliacoes'
    __table_args__ = (
        UniqueConstraint('usuario_id', 'receita_id', name='uix_usuario_receita_avaliacao'),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    nota: Mapped[float] = mapped_column(nullable=False)
    comentario: Mapped[Optional[str]] = mapped_column(Text)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable=False)
    receita_id: Mapped[int] = mapped_column(ForeignKey('receitas.id'), nullable=False)

    usuario: Mapped[Usuario] = relationship(back_populates='avaliacoes')
    receita: Mapped[Receita] = relationship(back_populates='avaliacoes')


class Favorito(Base):
    """Tabela de receitas favoritas dos usuários."""
    __tablename__ = 'favoritos'
    __table_args__ = (
        UniqueConstraint('usuario_id', 'receita_id', name='uix_usuario_receita_favorito'),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey('usuarios.id'), nullable=False)
    receita_id: Mapped[int] = mapped_column(ForeignKey('receitas.id'), nullable=False)

    usuario: Mapped[Usuario] = relationship(back_populates='favoritos')
    receita: Mapped[Receita] = relationship(back_populates='favoritos')
