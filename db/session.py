from core.config import DB_URL
from typing import Annotated
from sqlmodel import create_engine, Session
from fastapi import Depends

engine = create_engine(DB_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]