
from core.shared.spatial_randoms import random_point_coordinates, random_properties_set


def geojson_feature_collection_body(features: list) -> dict:
    return {
        "type": "FeatureCollection",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
            }
        },
        "features": features,
    }


def geojson_features_generator(number_of_features: int = 1):

    def geojson_point_geometry(coordinates: tuple[float, float]) -> dict:
        return {
            "type": "Point",
            "coordinates": coordinates
        }

    def geojson_properties(fid: int) -> dict:
        return {
            "fid": fid,
            **random_properties_set(year_range=(2000, 2023)),
        }

    for i in range(number_of_features):

        yield {
            "type": "Feature",
            "geometry": geojson_point_geometry(random_point_coordinates()),
            "properties": geojson_properties(fid=i)
        }
