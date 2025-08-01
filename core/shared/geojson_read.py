from core.shared.models_vectors import VectorEntity, VectorEntityFeature

def parse_geojson(geojson_data: dict) -> VectorEntity:
    crs = geojson_data.get("crs", {}).get("properties", {}).get("name", "")
    features = [
        VectorEntityFeature(
            geometry=feature.get("geometry", {}),
            properties=feature.get("properties", {})
        )
        for feature in geojson_data.get("features", [])
    ]
    return VectorEntity(crs=crs, features=features)
