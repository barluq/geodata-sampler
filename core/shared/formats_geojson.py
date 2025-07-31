
from core.shared.randoms import random_point_coordinates

def geojson_feature_collection_body(features):
    return {
        "type": "FeatureCollection",
        "crs": "urn:ogc:def:crs:OGC:1.3:CRS84",
        "features": {**features},
    }

def geojson_features_generator(number_of_features: int = 1):

    def geojson_point_geometry(coordinates: tuple[float, float]) -> dict:
        return {
            "type": "Point",
            "coordinates": coordinates
        }

    def geojson_property(fid: int, name: str) -> dict:
        return {
            "fid": fid,
            "name": name,
        }

    for i in range(number_of_features):

        properties = geojson_property(
            fid=i,
            name=f"Point {i}"
        )

        yield {
            "type": "Feature",
            "geometry": geojson_point_geometry(random_point_coordinates()),
            "properties": {**properties}
        }
