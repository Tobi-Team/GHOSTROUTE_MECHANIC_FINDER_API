from math import sqrt, cos, radians, sin, atan2
import pygeohash as pgh
import geohash


def convert_km_lat(km: float) -> float:
    """Converts Kilometer to latitude
    Args:
        km (float): Distance in kilometers
    Returns:
        float: Distance in degree latitude
    """
    DEGREE_LATITUDE = 111.32  # 1 degree of latitude in kilometers

    return round(km/DEGREE_LATITUDE, 5)


def convert_km_long(km: float, lat: float) -> float:
    """Converts Kilometer to longitude
    Args:
        km (float): Distance in kilometers
        lat (float): latitude in degrees
    Returns:
        float: Distance in degree longitude
    """
    DEGREE_LATITUDE = 111.32  # 1 degree of latitude in kilometers

    return round(km / (DEGREE_LATITUDE * cos(radians(lat))), 5)


def get_neighboring_grids(user_geohash: str) -> list[str]:
    neighbors = geohash.neighbors(user_geohash)
    return [user_geohash] + neighbors


def haversine(lat2: float, long2: float, lat1: float, long1: float) -> float:
    """Calculate the distance between 2 points on earth surface.

    Args:
        lat1 (float): Latitude of location 1
        long1 (float): Longitude of location 1
        lat2 (float): Latitude of location 2
        long2 (float): Longitude of location 2

    Returns:
        float: Distance between the 2 locations.
    """
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(long1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(long2)

    # Differences in coordinates
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = (
            sin(delta_lat / 2)**2 + cos(lat1_rad)
            * cos(lat2_rad) * sin(delta_lon / 2)**2
        )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance in kilometers
    distance = R * c

    return distance


def paginator(page: int, item_per_page: int) -> int:
    """
    Paginates the query results.

    Parameters:
        page (int): The page number.
        item_per_page (int): The number of items per page.

    Returns:
        int: The offset value.
    """
    return (page - 1) * item_per_page if page > 1 else 0
