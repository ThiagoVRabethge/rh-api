from sqlmodel import Field, Session, SQLModel, create_engine, select

class Candidate(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    date_of_birth: str = Field(index=True)