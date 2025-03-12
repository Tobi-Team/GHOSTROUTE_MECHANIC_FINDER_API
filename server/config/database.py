
import os
from typing import Iterator
from dotenv import load_dotenv
from sqlalchemy import create_engine, schema
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session,
)

from server.config.app_configs import app_configs


load_dotenv()

# for ci testing
environment = os.getenv("ENV", "test")

engine = (
    create_engine(
        app_configs.DB.TEST_DATABASE_URL
    )
    if environment == 'test'
    else create_engine(
        os.getenv("DATABASE_URL"),
        pool_size=10,
        max_overflow=5,
        pool_recycle=3600,
        isolation_level="READ COMMITTED",
        query_cache_size=500,
    )
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = (
    declarative_base()
    if environment == "test"
    else declarative_base(
        metadata=schema.MetaData(schema=app_configs.DB.SCHEMA)
    )
)
Base.query = scoped_session(SessionLocal).query_property()


def get_db() -> Iterator[Session]:
    try:
        db: Session = SessionLocal()
        yield db
    except Exception as e:
        raise e
    finally:
        db.expire_on_commit
        db.close()
