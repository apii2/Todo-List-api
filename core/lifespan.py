from sqlmodel import SQLModel
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from db.session import engine

def create_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield