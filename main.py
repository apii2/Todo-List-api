from fastapi import FastAPI
from sqlmodel import select
from core.lifespan import lifespan
from routes.todos import router as todo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://todo-list-one-omega-31.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router, prefix="/todos", tags=["Todos"])