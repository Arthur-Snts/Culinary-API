from models import Avaliacao, Receita, Usuario, Comentario, Favorito
from fastapi import HTTPException
from config import app
from typing import List
from statements import usuarios_all, post_usuario, update_usuario, delete_usuario # Statements de Usuários
from statements import receita_one, receitas_all, post_receita, update_receita, delete_receita # Statements de Receitas
from statements import favoritos_all, favoritos_usuario, post_favorito, delete_favorito # Statements de Favoritos
from statements import comentarios_all, comentario_usuario_receita, comentarios_receita, post_comentario, update_comentario, delete_comentario # Statements de Comentários
from statements import avaliacoes_all, avaliacoes_receita, avalicao_usuario_receita, post_avaliacao, update_avaliacao, delete_avaliacao # Statements de Avaliações
from statements import SessionDep


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #Usuarios
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


@app.get('/Usuarios')
def login_usuario(usu_email:str, usu_senha:str, session:SessionDep) -> Usuario | str:
    usuarios = usuarios_all(session=session)
    for usuario in usuarios:
        if usuario.email == usu_email:
            if usuario.senha == usu_senha:
                return usuario
        return {"mensagem": "Senha Incorreta"}
    return {"mensagem": "Email não Existe"}
            
# -------------------------------------------------------------------------------    

@app.post('/Usuarios')
def cadastra_usuario(usuario_cadastra:Usuario, session:SessionDep):
    usuarios = usuarios_all(session=session)
    for usuario in usuarios:
        if usuario.email == usuario_cadastra.email:
            raise HTTPException(400, "Email já Cadastrado")
    
    post_usuario(usuario=usuario_cadastra,session=session)
    return {"mensagem": "Usuário Cadastrado com sucesso"}
            
# -------------------------------------------------------------------------------          

@app.delete('/Usuarios')
def deleta_usuario(usuario_id:int, session:SessionDep):
    usuarios = usuarios_all(session=session)
    for usuario in usuarios:
        if usuario.id == usuario_id:
            delete_usuario(id=usuario_id, session=session)
            return {"mensagem": "Usuário deletado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")

# ------------------------------------------------------------------------------- 

@app.put('/Usuarios')
def atualiza_usuario(dados_novos:Usuario, session:SessionDep):
    usuarios = usuarios_all(session=session)
    for usuario in usuarios:
        if usuario.id == dados_novos.id:
            update_usuario(usuario=dados_novos,session=session)
            return {"mensagem": "Usuário Editado com sucesso"}
        
    raise HTTPException(404, "Usuário não Encontrado")
    


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #RECEITAS
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



@app.get('/Receitas/{nome}')
def lista_receita(nome:str, session:SessionDep) -> Receita:
    receita = receita_one(nome=nome, session=session)
    if receita != None:
        return receita
        
    raise HTTPException(404, "Receita não Encontrada")

# -------------------------------------------------------------------------------

@app.get('/Receitas')
def lista_receitas(session:SessionDep) -> List[Receita]:
    receitas = receitas_all(session=session)
    return receitas

# -------------------------------------------------------------------------------

@app.post('/Receitas')
def cadastra_receita(receita_cadastra:Receita, session:SessionDep):
    usuarios = usuarios_all(session=session)

    if not any(usuario.id == receita_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")
    
    receita = receita_one(nome=receita_cadastra.nome,session=session)
    if receita != None:
        raise HTTPException(409, "Nome já Cadastrado")
        
    post_receita(receita=receita_cadastra,session=session)
    return {"mensagem": "Receita Cadastrada com sucesso"}

# -------------------------------------------------------------------------------

@app.delete('/Receitas')
def deleta_receita(receita_id:int, session:SessionDep):
    receitas = receitas_all(session=session)
    for receita in receitas:
        if receita.id == receita_id:
            delete_receita(id=receita_id,session=session)
            return {"mensagem": "Receita deletada com sucesso"}
       
    raise HTTPException(404, "Receita não Encontrada")

# -------------------------------------------------------------------------------

@app.put('/Receitas')
def atualiza_receita( dados_novos:Receita, session:SessionDep):
    receitas = receitas_all(session=session)
    for receita in receitas:
        if receita.id == dados_novos.id:
            update_receita(receita=dados_novos,session=session)
            return {"mensagem": "Receita Atualizada com sucesso"}
        
    raise HTTPException(404, "Receita não Encontrada")



#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #FAVORITAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@app.get('/Favoritos/')
def lista_favoritos(usuario_id:int, session:SessionDep) -> List[Favorito]:

    favorito_dele = favoritos_usuario(id=usuario_id,session=session)
    
    
    if favorito_dele == []:
        raise HTTPException(404, "Usuário não Cadastrado ou não Possui Favoritos")
    else:
        return favorito_dele
    
# -------------------------------------------------------------------------------

@app.post('/Favoritos/')
def cadastra_favorito(favorito_cadastra:Favorito, session:SessionDep):

    usuarios = usuarios_all(session=session)
    if not any(usuario.id == favorito_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")
    
    receitas = receitas_all(session=session)
    if not any(receita.id == favorito_cadastra.receita_id for receita in receitas):
        raise HTTPException(404, "Receita não encontrada")
    
    favoritos = favoritos_usuario(id=favorito_cadastra.usuario_id, session=session)
    for favorito in favoritos:
        if favorito.receita_id == favorito_cadastra.receita_id:
            raise HTTPException(409, "Receita já Favoritada por esse Usuário")
        
    post_favorito(favorito=favorito_cadastra,session=session)
    return {"mensagem": "Favorito Cadastrado com sucesso"}

# -------------------------------------------------------------------------------

@app.delete('/Favoritos/')
def deleta_favorito(favorito_id:int, session:SessionDep):
    favoritos = favoritos_all(session=session)
    for favorito in favoritos:
        if favorito.id == favorito_id:
            delete_favorito(id=favorito_id,session=session)
            return {"mensagem": "Favorito deletado com sucesso"}
        
    raise HTTPException(404, "Favorito não Encontrado") 


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #AVALIAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
@app.get('/Avaliacoes/usuario-receita')
def lista_avaliacao_por_usuario_e_receita(usuario_id: int, receita_id: int, session:SessionDep) -> Avaliacao:
    avaliacao = avalicao_usuario_receita(rec_id=receita_id, usu_id=usuario_id, session=session)
    if avaliacao != None:
        return avaliacao

    raise HTTPException(404, "Avaliação não encontrada para este usuário e receita")

# -------------------------------------------------------------------------------
    
@app.get('/Avaliacoes/')
def lista_avaliacao_por_receita(receita_id: int, session:SessionDep) -> List[Avaliacao]:
    avaliacoes_da_receita = avaliacoes_receita(rec_id=receita_id, session=session)
    
    if avaliacoes_da_receita == []:
        raise HTTPException(404, "Nenhuma avaliação encontrada para esta receita")
    else:
        return avaliacoes_da_receita
    
# -------------------------------------------------------------------------------

@app.post('/Avaliacoes/')
def cadastra_avaliacao(avaliacao_cadastra: Avaliacao, session:SessionDep):
    usuarios = usuarios_all(session=session)
    if not any(usuario.id == avaliacao_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")
    receitas = receitas_all(session=session)
    if not any(receita.id == avaliacao_cadastra.receita_id for receita in receitas):
        raise HTTPException(404, "Receita não encontrada")
    
    avaliacao = avalicao_usuario_receita(rec_id=avaliacao_cadastra.receita_id, usu_id=avaliacao_cadastra.usuario_id,session=session)
    if avaliacao != None:
        raise HTTPException(409, "Receita já avaliada por esse usuário")
        
    post_avaliacao(avaliacao=avaliacao_cadastra,session=session)
    return {"mensagem": "Avaliação registrada com sucesso"}

# -------------------------------------------------------------------------------

@app.put('/Avaliacoes')
def atualiza_avaliacao(dados_novos: Avaliacao, session:SessionDep):
    avaliacao = avalicao_usuario_receita(rec_id=dados_novos.receita_id, usu_id=dados_novos.usuario_id,session=session)
    if avaliacao != None and avaliacao.id == dados_novos.id:
        update_avaliacao(avaliacao=dados_novos,session=session)
        return {"mensagem": "Avaliação atualizada com sucesso"}
    
    raise HTTPException(404, "Avaliação não encontrada para este usuário e receita")

# -------------------------------------------------------------------------------

@app.delete('/Avaliacoes/')
def deleta_avaliacao(avaliacao_id: int, session:SessionDep):
    avaliacoes = avaliacoes_all(session=session)
    for avaliacao in avaliacoes:
        if avaliacao.id == avaliacao_id:
            delete_avaliacao(id=avaliacao_id,session=session)
            return {"mensagem": "Avaliação deletada com sucesso"}
    
    raise HTTPException(404, "Avaliação não encontrada")


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                                        #COMENTAR
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
@app.get('/Comentarios/')
def lista_comentario_por_receita(receita_id: int, session:SessionDep) -> List[Comentario]:
    comentarios_da_receita = comentarios_receita(rec_id=receita_id, session=session)
    
    if comentarios_da_receita == []:
        raise HTTPException(404, "Nenhum comentário encontrado para esta receita")
    else:
        return comentarios_da_receita

# -------------------------------------------------------------------------------
    
@app.get('/Comentarios/usuario-receita')
def lista_comentario_por_usuario_e_receita(usuario_id: int, receita_id: int, session:SessionDep) -> Comentario:

    comentario = comentario_usuario_receita(usu_id=usuario_id, rec_id= receita_id, session=session)
    if comentario != None:
        return comentario

    raise HTTPException(404, "Comentário não encontrado para este usuário e receita")

# -------------------------------------------------------------------------------
    
@app.post('/Comentarios/')
def cadatra_comentario(comentario_cadastra: Comentario, session:SessionDep):
    usuarios= usuarios_all(session=session)
    if not any(usuario.id == comentario_cadastra.usuario_id for usuario in usuarios):
            raise HTTPException(404, "Usuário não encontrado")
    receitas = receitas_all(session=session)
    if not any(receita.id == comentario_cadastra.receita_id for receita in receitas):
        raise HTTPException(404, "Receita não encontrada")
    
    comentario = comentario_usuario_receita(usu_id=comentario_cadastra.usuario_id, rec_id= comentario_cadastra.receita_id,session=session)
    if comentario != None:
            raise HTTPException(409, "Receita já comentada por esse usuário")
    
    post_comentario(comentario=comentario_cadastra,session=session)
    return {"mensagem": "Comentário criado com sucesso"}

# -------------------------------------------------------------------------------
    
@app.put('/Comentarios/')
def atualiza_comentario(dados_novos: Comentario, session:SessionDep):
    comentario = comentario_usuario_receita(rec_id=dados_novos.receita_id, usu_id=dados_novos.usuario_id, session=session)
    if comentario != None and comentario.id == dados_novos.id:
        update_comentario(comentario=dados_novos,session=session)
        return {"mensagem": "Comentário atualizado com sucesso"}
    
    raise HTTPException(404, "Comentário não encontrado")

# -------------------------------------------------------------------------------
    
@app.delete('/Comentarios/')
def deleta_comentario(comentario_id: int, session:SessionDep):
    comentarios = comentarios_all(session=session)
    for comentario in comentarios:
        if comentario.id == comentario_id:
            delete_comentario(id=comentario_id, session=session)
            return {"mensagem": "Comentário deletado com sucesso"}
    
    raise HTTPException(404, "Comentário não encontrado")

# -------------------------------------------------------------------------------


    











