from models import Usuario, Receita, Favorito,Comentario,Avaliacao
from fastapi import FastAPI,HTTPException
from typing import List


app = FastAPI()

usuarios:List[Usuario] = []
receitas:List[Receita] = []
favoritos:List[Favorito] = []
comentarios:List[Comentario] = []
avaliacoes:List[Avaliacao] = []



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #Usuarios
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@app.post('/Usuarios')
def cadastra_usuario(usuario_cadastra:Usuario):
    for usuario in usuarios:
        if usuario.email == usuario_cadastra.email:
            raise HTTPException(400, "Email já Cadastrado")
    
    usuarios.append(usuario_cadastra)
    return {"mensagem": "Usuário Cadastrado com sucesso"}
            
# -------------------------------------------------------------------------------          

@app.delete('/Usuarios')
def deleta_usuario(usuario_id:int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário deletado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")

# ------------------------------------------------------------------------------- 

@app.put('/Usuarios')
def atualiza_usuario(dados_novos:Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == dados_novos.id:
            usuarios[i] = dados_novos
            return {"mensagem": "Usuário Editado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")
    


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #RECEITAS
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@app.get('/Receitas/{nome}',response_model=Receita)
def lista_receita(nome:str):
    for receita in receitas:
        if receita.nome == nome:
            return receita
        
    raise HTTPException(404, "Receita não Encontrada")

# -------------------------------------------------------------------------------

@app.get('/Receitas',response_model=List[Receita])
def lista_receitas():
    return receitas

# -------------------------------------------------------------------------------

@app.post('/Receitas')
def cadastra_receita(receita_cadastra:Receita):
    for receita in receitas:
        if receita.nome == receita_cadastra.nome:
            raise HTTPException(409, "Nome já Cadastrado")
        
    receitas.append(receita_cadastra)
    return {"mensagem": "Receita Cadastrada com sucesso"}

# -------------------------------------------------------------------------------

@app.delete('/Receitas')
def deleta_receita(receita_id:int):
    for receita in receitas:
        if receita.id == receita_id:
            receitas.remove(receita)
            return {"mensagem": "Receita deletada com sucesso"}
       
    raise HTTPException(404, "Receita não Encontrada")

# -------------------------------------------------------------------------------

@app.put('/Receitas')
def atualiza_receita( dados_novos:Receita):
    for i, receita in enumerate(receitas):
        if receita.id == dados_novos.id:
            receitas[i] = dados_novos
            return {"mensagem": "Receita Atualizada com sucesso"}
        
    raise HTTPException(404, "Receita não Encontrada")



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #FAVORITAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.get('/Favoritar/',response_model=List[Favorito])
def lista_favoritos(usuario_id:int):
    favorito_dele:List[Favorito] = []
    for favorito in favoritos:
        if favorito.usuario_id == usuario_id:
            favorito_dele.append(favorito)
    
    if favorito_dele == []:
        raise HTTPException(404, "Usuário não Cadastrado ou não Possui Favoritos")
    else:
        return favorito_dele
    
# -------------------------------------------------------------------------------

@app.post('/Favoritar/')
def cadastra_favorito(favorito_cadastra:Favorito):
    for favorito in favoritos:

        if not any(usuario.id == favorito_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")

        if not any(receita.id == favorito_cadastra.receita_id for receita in receitas):
            raise HTTPException(404, "Receita não encontrada")
        
        if favorito.usuario_id == favorito_cadastra.usuario_id and favorito.receita_id == favorito_cadastra.receita_id:
            raise HTTPException(409, "Receita já Favoritada por esse Usuário")
        
    favoritos.append(favorito_cadastra)
    return {"mensagem": "Favorito Cadastrado com sucesso"}

# -------------------------------------------------------------------------------

@app.delete('/Favoritar/')
def deleta_favorito(favorito_id:int):
    for favorito in favoritos:
        if favorito.id == favorito_id:
            favoritos.remove(favorito)
            return {"mensagem": "Favorito deletado com sucesso"}
        
    raise HTTPException(404, "Favorito não Encontrado") 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #AVALIAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
@app.get('/Avaliar/usuario-receita', response_model=Avaliacao)
def lista_avaliacao_por_usuario_e_receita(usuario_id: int, receita_id: int):
    for avaliacao in avaliacoes:
        if avaliacao.usuario_id == usuario_id and avaliacao.receita_id == receita_id:
            return avaliacao

    raise HTTPException(404, "Avaliação não encontrada para este usuário e receita")

# -------------------------------------------------------------------------------
    
@app.get('/Avaliar/', response_model=List[Avaliacao])
def lista_avaliacao_por_receita(receita_id: int):
    avaliacoes_da_receita: List[Avaliacao] = []

    for avaliacao in avaliacoes:
        if avaliacao.receita_id == receita_id:
            avaliacoes_da_receita.append(avaliacao)
    
    if avaliacoes_da_receita == []:
        raise HTTPException(404, "Nenhuma avaliação encontrada para esta receita")
    else:
        return avaliacoes_da_receita
    
# -------------------------------------------------------------------------------

@app.post('/Avaliar/')
def cadastra_avaliacao(avaliacao_cadastra: Avaliacao):
    if not any(usuario.id == avaliacao_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")

    if not any(receita.id == avaliacao_cadastra.receita_id for receita in receitas):
        raise HTTPException(404, "Receita não encontrada")
    for avaliacao in avaliacoes:
        if avaliacao.usuario_id == avaliacao_cadastra.usuario_id and avaliacao.receita_id == avaliacao_cadastra.receita_id:
            raise HTTPException(409, "Receita já avaliada por esse usuário")
        
    avaliacoes.append(avaliacao_cadastra)
    return {"mensagem": "Avaliação registrada com sucesso"}

# -------------------------------------------------------------------------------

@app.put('/Avaliar')
def atualiza_avaliacao(dados_novos: Avaliacao):
    for i, avaliacao in enumerate(avaliacoes):
        if avaliacao.usuario_id == dados_novos.usuario_id and avaliacao.receita_id == dados_novos.receita_id:
            avaliacoes[i] = dados_novos
            return {"mensagem": "Avaliação atualizada com sucesso"}
    
    raise HTTPException(404, "Avaliação não encontrada para este usuário e receita")

# -------------------------------------------------------------------------------

@app.delete('/Avaliar/')
def deleta_avaliacao(avaliacao_id: int):
    for avaliacao in avaliacoes:
        if avaliacao.id == avaliacao_id:
            avaliacoes.remove(avaliacao)
            return {"mensagem": "Avaliação deletada com sucesso"}
    
    raise HTTPException(404, "Avaliação não encontrada")


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #COMENTAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
@app.get('/Comentar/', response_model=List[Comentario])
def lista_comentario_por_receita(receita_id: int):
    comentarios_da_receita: List[Comentario] = []

    for comentario in comentarios:
        if comentario.receita_id == receita_id:
            comentarios_da_receita.append(comentario)
    
    if comentarios_da_receita == []:
        raise HTTPException(404, "Nenhum comentário encontrado para esta receita")
    else:
        return comentarios_da_receita

# -------------------------------------------------------------------------------
    
@app.get('/Comentar/usuario-receita', response_model=Comentario)
def lista_comentario_por_usuario_e_receita(usuario_id: int, receita_id: int):
    for comentario in comentarios:
        if comentario.usuario_id == usuario_id and comentario.receita_id == receita_id:
            return comentario

    raise HTTPException(404, "Comentário não encontrado para este usuário e receita")

# -------------------------------------------------------------------------------
    
@app.post('/Comentar/')
def cadatra_comentario(comentario_cadastra: Comentario):
    if not any(usuario.id == comentario_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")

    if not any(receita.id == comentario_cadastra.receita_id for receita in receitas):
        raise HTTPException(404, "Receita não encontrada")
    for comentario in comentarios:
        if comentario.id == comentario_cadastra.id:
            raise HTTPException(400, "Comentário com esse ID já existe")
    
    comentarios.append(comentario_cadastra)
    return {"mensagem": "Comentário criado com sucesso"}

# -------------------------------------------------------------------------------
    
@app.put('/Comentar/')
def atualiza_comentario(dados_novos: Comentario):
    for i, comentario in enumerate(comentarios):
        if comentario.id == dados_novos.id:
            comentarios[i] = dados_novos
            return {"mensagem": "Comentário atualizado com sucesso"}
    
    raise HTTPException(404, "Comentário não encontrado")

# -------------------------------------------------------------------------------
    
@app.delete('/Comentar/')
def deleta_comentario(comentario_id: int):
    for comentario in comentarios:
        if comentario.id == comentario_id:
            comentarios.remove(comentario)
            return {"mensagem": "Comentário deletado com sucesso"}
    
    raise HTTPException(404, "Comentário não encontrado")

# -------------------------------------------------------------------------------


    











