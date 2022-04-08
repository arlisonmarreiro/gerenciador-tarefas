from typing import List, Dict, Any


class BaseDados:
    base_de_dados: List[Dict[str, Any]] = [
    {"id":1, "titulo":"Estudar Python", "descricao":"Estudar Python para exercitar a lógica", "status":"a fazer"},
    {"id":2, "titulo":"Estudar Selenium", "descricao":"Estudar Selenium para fazer testes automatizados", "status":"feito"},
    {"id":3, "titulo":"Estudar TDD", "descricao":"Estudar TDD para melhorar o processo de desenvolvimento", "status":"fazendo"},

    ]

    id_atual = 3

    def listar(self):
        return self.base_de_dados

    def inserir(self, tarefa: Dict[str, Any]) -> Dict[str, Any]:
        self.id_atual +=1
        tarefa["id"] = self.id_atual
        self.base_de_dados.append(tarefa)
        return tarefa

