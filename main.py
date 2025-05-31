from models import Usuario, Receita, Favorito
from fastapi import FastAPI,HTTPException
from typing import List


app = FastAPI()

usuarios:List[Usuario] = []
receitas:List[Receita] = []
favoritos:List[Favorito] = []

@app.post('/Usuarios')
def cadastra_usuario(usuario_cadastra:Usuario):
    for usuario in usuarios:
        if usuario.email == usuario_cadastra.email:
            raise HTTPException(404, "Email já Cadastrado")
    
    usuarios.append(usuario_cadastra)
    return {"mensagem": "Usuário Cadastrado com sucesso"}
            
            


@app.delete('/Usuarios')
def deleta_usuario(usuario_id:int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário deletado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")

@app.put('/Usuarios')
def atualiza_usuario(dados_novos:Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == dados_novos.id:
            usuarios[i] = dados_novos
            return {"mensagem": "Usuário Editado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")

# -------------------------------------------------------------------------------


@app.get('/Receitas/{nome}',response_model=Receita)
def lista_receita(nome:str):
    for receita in receitas:
        if receita.nome == nome:
            return receita
        
    raise HTTPException(404, "Receita não Encontrada")

@app.get('/Receitas',response_model=List[Receita])
def lista_receitas():
    return receitas

@app.post('/Receitas')
def cadastra_receita(receita_cadastra:Receita):
    for receita in receitas:
        if receita.nome == receita_cadastra.nome:
            raise HTTPException(404, "Nome já Cadastrado")
        
    receitas.append(receita_cadastra)
    return {"mensagem": "Receita Cadastrada com sucesso"}

@app.delete('/Receitas')
def deleta_receita(receita_id:int):
    for receita in receitas:
        if receita.id == receita_id:
            receitas.remove(receita)
            return {"mensagem": "Receita deletada com sucesso"}
       
    raise HTTPException(404, "Receita não Encontrada")

@app.put('/Receitas')
def atualiza_receita( dados_novos:Receita):
    for i, receita in enumerate(receitas):
        if receita.id == dados_novos.id:
            receitas[i] = dados_novos
            return {"mensagem": "Receita Atualizada com sucesso"}
        
    raise HTTPException(404, "Receita não Encontrada")



# -------------------------------------------------------------------------------


@app.get('/Favoritar/',response_model=List[Favorito])
def listar_favoritos(usuario_id:int):
    favorito_dele:List[Favorito] = []
    for favorito in favoritos:
        if favorito.usuario_id == usuario_id:
            favorito_dele.append(favorito)
    
    if favorito_dele == []:
        raise HTTPException(404, "Usuário não Cadastrado ou não Possui Favoritos")
    else:
        return favorito_dele

@app.post('/Favoritar/')
def cadastrar_favorito(favorito_cadastra:Favorito):
    for favorito in favoritos:
        if favorito.usuario_id == favorito_cadastra.usuario_id and favorito.receita_id == favorito_cadastra.receita_id:
            raise HTTPException(404, "Receita já Favoritada por esse Usuário")
        
    favoritos.append(favorito_cadastra)
    return {"mensagem": "Favorito Cadastrado com sucesso"}

@app.delete('/Favoritar/')
def deleta_favorito(favorito_id:int):
    for favorito in favoritos:
        if favorito.id == favorito_id:
            favoritos.remove(favorito)
            return {"mensagem": "Favorito deletado com sucesso"}
        
    raise HTTPException(404, "Favorito não Encontrado")