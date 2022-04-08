from fastapi import FastAPI
from .modelos import Tarefa
from typing import List, Dict, Any
from .data import BaseDados

base_de_dados = BaseDados()


def inserir(self, tarefa: Tarefa) -> Tarefa:
        self.id_atual += 1
        tarefa["id"] = self.id_atual
        self.a_fazer.append(tarefa)
        return tarefa 
    
app = FastAPI()


@app.get("/")
def home():
    """
    View para a home da aplicação
    """
    return {"message": "Hello World"}

@app.get("/tarefas", response_model=List[Tarefa])
def listar():
    """
    View para listar todas as tarefas
    """
    return base_de_dados.listar()

@app.post("/tarefas", response_model=Tarefa, status_code=201)
def inserir_tarefa(tarefa: Tarefa):
    """
    View para inserir uma nova tarefa
    """
    return base_de_dados.inserir(tarefa.dict())



  




