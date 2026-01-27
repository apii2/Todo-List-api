from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id:int|None = Field(default=None, primary_key=True)
    name:str = Field(index=True, nullable=False, min_length=3, max_length=100)
    completed:bool = Field(default=False)