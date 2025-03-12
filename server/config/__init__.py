from server.config.database import Base, get_db, engine
from server.config.app_configs import app_configs


def init_db():
    Base.metadata.create_all(bind=engine)
    return True


__all__ = [
    "Base",
    "get_db",
    "engine",
    "init_db",
    "app_configs"
]
