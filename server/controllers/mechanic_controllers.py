from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..config import get_db
from ..services.services import Services
from ..schemas import (
    APIResponse,
    ServiceResultModel,
    PagedResponse
)
from ..schemas.mechanic_schemas import (
    GetMechQuery,
    GetMechanics,
    UpdateMechSchema
)


router = APIRouter(prefix='/mechanics', tags=['Mechanics'])


# Admin routes
# @router.post('/add')
# async def add_mechanic(
#     data: dict,
#     db: Session = Depends(get_db)
# ) -> APIResponse:
#     """Add a new mechanic"""
#     ...


# @router.put('/update')
# async def update_mechanic(
#     data: UpdateMechSchema,
#     db: Session = Depends(get_db)
# ) -> APIResponse:
#     """Update a mechanic"""
#     ...


# @router.delete('/delete')
# async def delete_mechanic(
#     data: dict,
#     db: Session = Depends(get_db)
# ) -> APIResponse:
#     """Delete a mechanic"""
#     ...


# Client routes
@router.get('/search')
async def search(
    lat: float,
    long: float,
    radius: float,
    db: Session = Depends(get_db)
) -> APIResponse:
    """Search for mechanics"""
    service = Services(db)
    result = await service.search(lat, long, radius)
    return APIResponse(data=result.data)


@router.get('/get')
async def get_mechanics(
    query: GetMechQuery = Depends(),
    db: Session = Depends(get_db)
) -> APIResponse:
    """Get mechanics"""
    service = Services(db)
    result = await service.get_mechanics(query.model_dump())
    return APIResponse(data=result.data)
