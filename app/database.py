import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os

DATABASE_URL = "postgresql://postgres:postgres@biblioteca_api-fastapi_postgres-1:5432/biblioteca"

engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()

# Crear tablas si no existen
def create_db():
    Base.metadata.create_all(bind=engine)
