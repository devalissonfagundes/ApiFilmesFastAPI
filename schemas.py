from pydantic import BaseModel

class FilmeBase(BaseModel):
    titulo: str
    genero: str
    ano: int
    nota: float

class FilmeCreate(FilmeBase):
    pass 

class filme (FilmeCreate):
    id_filmes: int

    class Config:
        orm_mode = True
