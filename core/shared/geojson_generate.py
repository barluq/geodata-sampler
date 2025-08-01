
from typing import Generator, Literal
from core.shared.spatial_randoms import random_point_coordinates, random_properties_set, random_properties_set_per_year


def geojson_feature_collection_body(features: list) -> dict:
    """
    Creates a GeoJSON FeatureCollection dictionary with the specified features.

    Args:
        features (list): A list of GeoJSON feature dictionaries to include in the FeatureCollection.

    Returns:
        dict: A dictionary representing a GeoJSON FeatureCollection with the provided features and a CRS of "urn:ogc:def:crs:OGC:1.3:CRS84".
    """
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


def geojson_features_generator(
        number_of_features: int, 
        attributes: dict[str, Literal["string", "integer", "float"]],
        timeseries_attributes: dict[str, Literal["string", "integer", "float"]] | None = None,
        year_range: tuple[int, int] | None = None
        ) -> Generator[dict, None, None]:
    
    """
    Generates a sequence of GeoJSON features with random point coordinates and properties.
    Args:
        number_of_features (int): The number of GeoJSON features to generate.
        attributes (dict[str, Literal["string", "integer", "float"]]): A dictionary
            defining the attributes of the features, where keys are attribute names and values are their types.
        year_range (tuple[int, int] | None): A tuple defining the range of years
            for which properties should be generated. If None, properties are generated without year consideration.
    """

    def geojson_point_geometry(coordinates: tuple[float, float]) -> dict:
        """
        Creates a GeoJSON Point geometry dictionary from the given coordinates.

        Args:
            coordinates (tuple[float, float]): A tuple representing the (longitude, latitude) of the point.

        Returns:
            dict: A dictionary representing the GeoJSON Point geometry.

        Example:
            >>> geojson_point_geometry((12.34, 56.78))
            {'type': 'Point', 'coordinates': (12.34, 56.78)}
        """
        return {
            "type": "Point",
            "coordinates": coordinates
        }

    def geojson_properties(fid: int) -> dict:
        """
        Generates a dictionary of GeoJSON properties for a given feature ID.

        Parameters:
            fid (int): The feature ID.

        Returns:
            dict: A dictionary containing the feature ID and additional properties.
                  If 'year_range' is None, properties are generated using 'random_properties_set'.
                  Otherwise, properties are generated per year using 'random_properties_set_per_year'.

        Note:
            This function relies on the variables 'attributes' and 'year_range' being defined in the enclosing scope.
        """
        
        features_result: dict = {
            "fid": fid,
            **random_properties_set(attributes=attributes)
            }

        # If year_range and timeseries_attributes are provided, generate properties for each year in the range
        if year_range is not None and timeseries_attributes is not None:
            features_result = {
                **features_result,
                **random_properties_set_per_year(
                    attributes=timeseries_attributes,
                    year_range=year_range
                )
            }

        return features_result

    for i in range(number_of_features):
        yield {
            "type": "Feature",
            "geometry": geojson_point_geometry(random_point_coordinates()),
            "properties": geojson_properties(fid=i)
        }
