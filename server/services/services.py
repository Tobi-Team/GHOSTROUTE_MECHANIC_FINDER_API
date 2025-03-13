from sqlalchemy.orm import Session

from ..repositories import Adapter
from ..schemas import ServiceResultModel
from ..schemas.mechanic_schemas import (
    GetMechSchema,
    GetMechanics,
    GetMechSchemaPartial
)


class Services:
    def __init__(self, db: Session) -> None:
        self.repo = Adapter(db).mech_repo
        self.geo_repo = Adapter(db).geo_repo

    async def search(
        self, lat: float, long: float, radius: float
    ) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            mechs = await self.repo.get_by_loc(lat, long, radius)
            result.data = mechs
            return result
        except Exception as exc:
            raise exc

    async def get_mechanics(self, filters: dict = None) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            if filters:
                paged_response = await self.repo.get_all(filters)
            else:
                paged_response = await self.repo.get_all()
            data = [
                GetMechSchemaPartial.model_validate(mech).model_dump(
                    exclude_unset=True
                )
                for mech in paged_response.data
            ]
            paged_response.data = data
            result.data = paged_response
            return result
        except Exception as exc:
            raise exc

    async def get_mech_by_id(self, id) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            mech = await self.repo.get_by_id(id)
            result.data = GetMechSchemaPartial.model_validate(mech)
            return result
        except Exception as exc:
            raise exc

    async def get_mech_extended_by_id(self, id) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            mech = await self.repo.get_by_id(id)
            result.data = GetMechSchema.model_validate(mech)
            return result
        except Exception as exc:
            raise exc
