from fastapi import FastAPI
from models import Todo 


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []


# get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# get single todo
@app.get("/todos/{todo_id}")
async def get_a_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}

# create a todo
@app.post("/todos")
async def create_todos(todo: Todo): # pydantic ... endpoint request body has to follow the Model 
    todos.append(todo)
    return {"message": "Todo has been added"}
