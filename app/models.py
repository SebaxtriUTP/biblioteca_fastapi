import datetime as _dt
import sqlalchemy as _sql

import database as _database

class Book(_database.Base):
    __tablename__ = "books"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, index=True)
    author = _sql.Column(_sql.String, index=True)
    year = _sql.Column(_sql.Integer, index=True)
    isbn = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)