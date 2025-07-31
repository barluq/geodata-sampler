import json
from pathlib import Path

def store_geojson_to_generated_folder(
    geojson_data: dict,
    filename: str,
) -> None:
    """
    Stores the provided GeoJSON data into a file within the '../../data/generated' directory.

    Args:
        geojson_data (dict): The GeoJSON data to be saved.
        filename (str): The name of the file to save the data as.

    Returns:
        None

    The function ensures that the output directory exists before writing the GeoJSON data to the specified file.
    """
    # Ensure the output directory exists
    output_dir = Path('../../data/generated')
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write the GeoJSON to a file
    output_path = output_dir / filename
    with open(output_path, 'w') as f:
        json.dump(geojson_data, f, indent=2)
