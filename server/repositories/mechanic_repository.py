from sqlalchemy.orm import Session
from server.models.geohash import GeoHashTable

from ..models.mechanics import Mechanics
from ..schemas.mechanic_schemas import GetMechSchema, GetMechSchemaPartial, GetMechanics
from ..repositories.repository import Repository
from ..utils import get_neighboring_grids, haversine


class MechanicRepository(Repository):
    """Mechanics repository"""

    def __init__(self, db: Session) -> None:
        self._Model = Mechanics
        super().__init__(self._Model, db)

    async def get_by_email(self, email: str) -> Mechanics:
        """Get a mech by email
        Args:
            email (str): mechs email
        Returns:
            Mechanics: mechanic model instance
        """
        try:
            mech = self.db.query(self._Model).filter_by(email=email).first()
        except Exception as e:
            raise e
        if not mech:
            return False
        return mech
    
    async def get_by_username(self, username: str) -> Mechanics:
        """Get a mech by username
        Args:
            username (str): mechs username
        Returns:
            Mechanics: mechanic model instance
        """
        try:
            mech = self.db.query(self._Model).filter_by(username=username).first()
        except Exception as e:
            raise e
        if not mech:
            return False
        return mech
    
    async def get_by_phone(self, phone: str) -> Mechanics:
        """Get a mech by phone
        Args:
            phone (str): mechs phone
        Returns:
            Mechanics: mechanic model instance
        """
        try:
            mech = self.db.query(self._Model).filter_by(phone=phone).first()
        except Exception as e:
            raise e
        if not mech:
            return False
        return mech

    async def get_by_loc(self, lat: float, long: float, radius: float) -> GetMechanics:
        """Get Mechanics by location
        Args:
            lat (float): The clients
            long (float): The client's Longitude
            radius (float): The search radius
        Raises:
            e: ...
        Returns:
            GetMechanics: GetMechanics instance
        """
        try:
            user_geohash = GeoHashTable.encode_geohash(lat, long, precision=6)
            
            grids_to_search = get_neighboring_grids(user_geohash)
            
            geo_mechs = self.db.query(GeoHashTable).filter(
                GeoHashTable.geohash.in_(grids_to_search)
            ).all()

            mech_schemas = []
            for mech in [await self.get_by_id(m.mech_id) for m in geo_mechs]:
                distance = haversine(
                    mech.location[0], mech.location[1], lat, long
                )
                mech_dict = mech.to_dict()
                mech_dict["distance"] = round(distance, 4)
                validated_mech = GetMechSchema.model_validate(mech_dict)
                mech_schemas.append(validated_mech)

            close_mechs = [mech for mech in mech_schemas if mech.distance <= radius]
            sorted_mechs = sorted(close_mechs, key=lambda x: x.distance)

            return GetMechanics(data=sorted_mechs, count=len(sorted_mechs))
        
        except Exception as e:
            raise e


class GeoHashRepository(Repository):
    """GeoHash repository"""

    def __init__(self, db: Session) -> None:
        self._Model = GeoHashTable
        super().__init__(self._Model, db)


__all__ = ["MechanicRepository", "GeoHashRepository"]
