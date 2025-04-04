from sqlalchemy.orm import Session

from ..repositories.mechanic_repository import (
    MechanicRepository,
    GeoHashRepository
)


class Adapter:
    def __init__(self, db: Session):
        self.mech_repo: MechanicRepository = MechanicRepository(db)
        self.geo_repo: GeoHashRepository = GeoHashRepository(db)
