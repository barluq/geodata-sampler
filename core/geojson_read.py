from .models_vectors import VectorEntity, VectorEntityFeature

def parse_geojson(geojson_data: dict) -> VectorEntity:
    """
    Parses a GeoJSON dictionary and returns a VectorEntity object.

    Args:
        geojson_data (dict): A dictionary representing the GeoJSON data.

    Returns:
        VectorEntity: An object containing the coordinate reference system (CRS) and a list of features extracted from the GeoJSON.

    Notes:
        - Expects the input dictionary to follow the GeoJSON FeatureCollection structure.
        - The CRS is extracted from 'crs.properties.name' if present; otherwise, an empty string is used.
        - Each feature in 'features' is converted to a VectorEntityFeature with its geometry and properties.
    """
    crs = geojson_data.get("crs", {}).get("properties", {}).get("name", "")
    features = [
        VectorEntityFeature(
            geometry=feature.get("geometry", {}),
            properties=feature.get("properties", {})
        )
        for feature in geojson_data.get("features", [])
    ]
    return VectorEntity(crs=crs, features=features)
