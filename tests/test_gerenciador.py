from ast import Pass
from fastapi.testclient import TestClient
from fastapi import status
from gerenciador_tarefas.data import BaseDados
from gerenciador_tarefas.gerenciador import app, base_de_dados



def test_quando_abrir_pagina_inicial_o_codigo_de_status_deve_ser_200():
    cliente = TestClient(app)
    resposta = cliente.get('/')
    assert resposta.status_code == status.HTTP_200_OK
    
def test_quando_listar_tarefas_devo_ter_como_retorno_codigo_de_status_200():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert resposta.status_code == status.HTTP_200_OK

def test_quando_listar_tarefas_o_formato_de_retorno_deve_ser_json():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert resposta.headers['Content-Type'] == 'application/json'

def test_quando_listar_tarefas_o_retorno_deve_ser_uma_lista():
    cliente = TestClient(app)
    resposta = cliente.get('/tarefas')
    assert isinstance(resposta.json(), list)


def test_recurso_tarefas_deve_aceitar_o_verbo_post():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas")
    assert resposta.status_code != status.HTTP_405_METHOD_NOT_ALLOWED

def test_quando_uma_tarefa_e_submetida_deve_possuir_um_titulo():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_titulo_da_tarefa_deve_conter_entre_3_e_50_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": 2 * "*"})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    resposta = cliente.post("/tarefas", json={"titulo": 51 * "*"})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_quando_uma_tarefa_e_submetida_deve_possuir_uma_descricao():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": "titulo"})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_descricao_da_tarefa_pode_conter_no_maximo_140_caracteres():
    cliente = TestClient(app)
    resposta = cliente.post("/tarefas", json={"titulo": "titulo", "descricao": "*" * 141})
    assert resposta.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY




















