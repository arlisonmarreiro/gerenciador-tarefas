from pydantic import BaseModel, constr
from typing import List, Dict, Any

class Tarefa(BaseModel):
    id: int
    titulo: constr(min_length=3, max_length=50)
    descricao: constr(max_length=140)
    status: str = None