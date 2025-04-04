from sqlalchemy import Column, String, Float, Integer, Boolean
from ..config import app_configs
from .basemodel import BaseModel
from sqlalchemy.types import JSON
from sqlalchemy.orm import relationship


class Mechanics(BaseModel):
    __tablename__ = "mechanics"
    __mapper_args__ = {"polymorphic_identity": "mechanics"}

    # Personals
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    whatsapp = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=True, unique=True, index=True)
    profile_image = Column(JSON, nullable=True)
    # password = Column(String, nullable=False)

    # Company/workshop related
    address = Column(String, nullable=False)
    verified = Column(Boolean, nullable=True, default=False)
    company_name = Column(String, nullable=True)
    company_contact = Column(String, nullable=True)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    company_image = Column(JSON, nullable=True)

    # Ratings/reviews
    contacted = Column(Integer, nullable=False, default=0)
    rating = Column(Float, nullable=False, default=0.0)  # ratings/5
    review = Column(JSON, nullable=True)

    # Professional
    speciality = Column(String, nullable=True)  # Speciality
    skills = Column(JSON, nullable=True)  # List of skills

    # Relationships
    geohash = relationship(
        "GeoHashTable",
        back_populates="mechanics",
        cascade="all, delete-orphan"
    )

    def __init__(
            self,
            first_name: str,
            last_name: str,
            address: str,
            state: str,
            country: str,
            phone: str,
            location: list[float, float] = [],
            verified: bool = False,
            ) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.state = state.capitalize()
        self.address = address
        self.country = country.capitalize()
        self.phone = phone
        self.verified = verified
        self.latitude = round(location[0], 5)
        self.longitude = round(location[1], 5)
