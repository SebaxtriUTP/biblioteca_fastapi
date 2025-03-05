import datetime as _dt
import pydantic as _pydantic

class _BaseBook(_pydantic.BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class Book(_BaseBook):
    id: int
    created_at: _dt.datetime
    updated_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes = True
class CreateBook(_BaseBook):
    pass