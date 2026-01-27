from fastapi import FastAPI
from sqlmodel import select
from core.lifespan import lifespan
from routes.todos import router as todo_router

app = FastAPI(lifespan=lifespan)

app.include_router(todo_router, prefix="/todos", tags=["Todos"])
