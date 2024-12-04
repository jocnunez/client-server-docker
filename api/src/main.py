print("Initializing ToDos API!")

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/todos")
def read_item():
    #TODO: consultar en base de datos mi lista de todos
    todos = [
                {"text": "tarea1", "check": "false"},
                {"text": "tarea2", "check": "false"},
                {"text": "tarea3", "check": "false"}
            ]
    return todos
