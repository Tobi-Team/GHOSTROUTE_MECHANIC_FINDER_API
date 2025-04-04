from fastapi import APIRouter

from ..config import app_configs
from ..controllers.mechanic_controllers import router as mech_route


router = APIRouter(prefix=app_configs.URI_PREFIX)
router.include_router(mech_route)
