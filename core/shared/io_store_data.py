import json
from pathlib import Path

def store_geojson_to_generated_folder(
    geojson_data: dict,
    folder_path: Path,
    filename: str,
) -> None:
    """
    Stores the provided GeoJSON data into a file within the specified folder path.

    Args:
        geojson_data (dict): The GeoJSON data to be saved.
        folder_path (Path): The folder path where the file will be saved.
        filename (str): The name of the file to save the data as.

    Returns:
        None

    The function ensures that the output directory exists before writing the GeoJSON data to the specified file.
    """
    # Ensure the output directory exists
    folder_path.mkdir(parents=True, exist_ok=True)

    # Write the GeoJSON to a file (this will overwrite if file exists)
    output_path = folder_path / filename
    with open(output_path, 'w') as f:
        json.dump(geojson_data, f, indent=2)
