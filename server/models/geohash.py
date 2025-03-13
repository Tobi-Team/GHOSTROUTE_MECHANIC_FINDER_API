import uuid
from sqlalchemy import UUID, Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ..config import Base
import pygeohash as pgh


class GeoHashTable(Base):
    __tablename__ = "geohash"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    geohash = Column(String, nullable=False, index=True, unique=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    mech_id = Column(UUID(as_uuid=True), ForeignKey("mechanics.id", ondelete="CASCADE"), nullable=False)

    mechanics = relationship("Mechanics", back_populates="geohash")
    
    def __init__(self, geohash: str, mech_id: str) -> None:
        self.geohash = geohash
        self.latitude = self.decode_geohash(self.geohash)[0]
        self.longitude = self.decode_geohash(self.geohash)[1]
        self.mech_id = mech_id

    @staticmethod
    def encode_geohash(latitude: float, longitude: float, precision: int = 6) -> str:
        return pgh.encode(latitude, longitude, precision)

    @staticmethod
    def decode_geohash(geohash: str) -> tuple[float, float]:
        return pgh.decode(geohash)