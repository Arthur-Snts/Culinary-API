from models import Usuario, Receita, Favorito
from fastapi import FastAPI
from typing import List


app = FastAPI()

usuarios:List[Usuario] = []
receitas:List[Receita] = []
favoritos:List[Favorito] = []

@app.post('/Usuarios')
def cadastra_usuario():
    pass

@app.delete('/Usuarios')
def deleta_usuario():
    pass

@app.put('/Usuarios')
def atualiza_usuario():
    pass

# -------------------------------------------------------------------------------


@app.get('/Receitas/{nome}')
def lista_receita():
    pass

@app.get('/Receitas')
def lista_receitas():
    pass

@app.post('/Receitas')
def cadastra_receita():
    pass

@app.delete('/Receitas')
def deleta_receita():
    pass

@app.put('/Receitas')
def atualiza_receita():
    pass



# -------------------------------------------------------------------------------


@app.get('/Favoritar')
def listar_favoritos():
    pass

@app.post('/Favoritar')
def cadastrar_favorito():
    pass

@app.delete('/Favoritar')
def deleta_favorito():
    pass