from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Tarefa(BaseModel):
    descricao : str
    responsavel : str | None
    nivel : int
    situacao : str | None
    prioridade : int

tarefas=list[Tarefa]=[]



#adicionar uma nova tarefa na lista 

@app.post('/tarefas/criar', status_code=status.HTTP_201_CREATED) 
def nova_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)

    return tarefas


#atualizar uma tarefa pelo seu (nivel, descricao), nova & em andamento & pendente & cancelada & resolvido
#atualizar as tarefas 

'''em andamento '''
@app.put('/tarefa/{tarefa_nivel}')
def atualizar_tarefa(tarefa_nivel: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.descricao == 'NOVA' or tarefa_atual.descricao == 'PENDENTE':
            tarefa_atual.descricao == 'EM ANDAMENTO'
            return tarefas
        else:
            return f'Tarefa nao pode ser resolvida'

    raise HTTPException(404,  detail="Tarefa não encontrada")

'''pendente '''
@app.put('/tarefa/{tarefa_nivel}')
def atualizar_tarefa(tarefa_nivel: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.descricao == 'NOVA' or tarefa_atual.descricao == 'EM ANDAMENTO':
            tarefa_atual.descricao == 'RESOLVIDA'
            return tarefas
        else:
            return f'Tarefa nao pode ser resolvida'

    raise HTTPException(404,  detail="Tarefa não encontrada")

'''cancelada'''
@app.put('/tarefa/{tarefa_nivel}')
def atualizar_tarefa(tarefa_nivel: int):
    for tarefa_atual in tarefas:
        tarefa_atual.descricao == 'CANCELADA'
        return tarefas
        
    raise HTTPException(404,  detail="Tarefa não encontrada")


'''resolvida '''
@app.put('/tarefa/{tarefa_nivel}')
def atualizar_tarefa(tarefa_nivel: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.descricao == 'EM ANDAMENTO':
            tarefa_atual.descricao == 'RESOLVIDA'
            return tarefas
        else:
            return f'Tarefa nao pode ser resolvida'

    raise HTTPException(404,  detail="Tarefa não encontrada")




# deletar uma tarefa pelo seu nivel


@app.delete("/tarefa/{tarefa_nivel}")
def remove_tarefa(tarefa_nivel: int):
    for tarefa_atual in tarefas:
        if tarefa_atual.nivel == tarefa_nivel:
            tarefas.remove(tarefa_atual)

    raise HTTPException(404, detail="Tarefa não encontrad")  



#buscar todas as tarefas de uma so vez

@app.get('/tarefa')
def obter_tarefas():
    return tarefas



#buscar por nivel

@app.get('/tarefa/{tarefa_nivel}')
def obter_uma_tarefa(tarefa_nivel: int, response: Response):
    for tarefa in tarefas:
        if tarefa.nivel == tarefa_nivel:
            return tarefas

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Tarefa nao foi encontrada = {tarefa_nivel}')           


#buscar tarefa por prioridade

@app.get('/tarefa/{tarefa_prioridade}')
def obter_uma_tarefa(tarefa_prioridade: int, response: Response):
    for tarefa in tarefas:
        if tarefa.prioridade == tarefa_prioridade:
            return tarefas

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Tarefa nao foi encontrada = {tarefa_prioridade}')                         



#busca tarefa por status


@app.get('/tarefa/{tarefa_situacao}')
def obter_uma_tarefa(tarefa_situacao: str, response: Response):
    for tarefa in tarefas:
        if tarefa.situacao == tarefa_situacao or tarefa.situacao == None:
            return tarefas

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Tarefa nao foi encontrada = {tarefa_situacao}')   
