from datetime import datetime
from fastapi import Query
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

from ..config import app_configs
from ..schemas import PagedQuery


class GetMechQuery(PagedQuery):
    id: Optional[str] = Query(None, description="Search by id")
    phone: Optional[str] = Query(None, description="Search by phone number")
    email: Optional[str] = Query(None, description="Search by email")


class GetMechSchemaPartial(BaseModel):
    model_config = {"from_attributes": True, "extra": "ignore"}
    id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    first_name: str
    last_name: str
    company_name: Optional[str]
    verified: bool
    rating: Optional[float]
    review: Optional[list[str]]
    skills: Optional[list[str]]
    contacted: Optional[int]
    distance: Optional[float] = Field(default=None)


class GetMechSchema(GetMechSchemaPartial):
    phone: Optional[str]
    whatsapp: Optional[str] = Field(default=None)
    country: str
    state: str
    email: str
    address: str
    location: Optional[list]
    longitude: Optional[float]
    latitude: Optional[float]
    company_contact: Optional[str]
    speciality: Optional[str]


class GetMechanics(BaseModel):
    model_config = {"from_attributes": True, "extra": "ignore"}
    data: list[GetMechSchemaPartial | None]
    count: int | None


class UpdateMechSchema(BaseModel):
    model_config = {"from_attributes": True, "extra": "ignore"}
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    whatsapp: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)
    address: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    state: Optional[str] = Field(default=None)
    speciality: Optional[str] = Field(default=None)
    contacted: Optional[int] = Field(default=None)
    company_name: Optional[str] = Field(default=None)


class UpdateReviewSchema(BaseModel):
    model_config = {"from_attributes": True, "extra": "ignore"}
    rating: Optional[int]
    review: Optional[str]


class GeoHashSchema(BaseModel):
    geohash: str = Field(min_length=1, max_length=12)
    mech_id: str = Field(min_length=1, max_length=255)
