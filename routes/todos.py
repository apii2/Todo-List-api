from schemas.todo import TodoResponse, TodoCreate, TodoUpdate
from models.todo import Todo
from db.session import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select

router = APIRouter()

@router.get("/", response_model=TodoResponse) 
def getTodos(session: SessionDep):
    return {"message": "Todos retrieved successfully", "results": session.exec(select(Todo)).all()}

@router.post("/create")
def postTodo(todo_data: TodoCreate, session: SessionDep):
    todo = Todo(**todo_data.model_dump())
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return {"message": "Todo created successfully"}

@router.delete("/{todo_id}/delete")
def deleteTodo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted successfully"}

@router.patch("/{todo_id}/update", response_model=TodoResponse)
def toggleCompleted(todo_id: int, todo_data: TodoUpdate, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail={"error": "Todo not found"})
    todo.sqlmodel_update(todo_data.model_dump(exclude_unset=True))
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return {"message": "Todo updated successfully!", "results": [todo]}