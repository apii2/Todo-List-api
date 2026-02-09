from sqlmodel import SQLModel

class TodoList(SQLModel):
    id:int
    name:str
    completed:bool
    
class TodoResponse(SQLModel):
    message:str
    results:list[TodoList]
    
class TodoCreate(SQLModel):
    name:str
    
class TodoUpdate(SQLModel):
    completed:bool 