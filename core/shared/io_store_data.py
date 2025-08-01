import json
from pathlib import Path

def read_geojson_from_file(file_path: Path) -> dict:
    """
    Reads GeoJSON data from a file and returns it as a dictionary.

    Args:
        file_path (Path): The path to the GeoJSON file.

    Returns:
        dict: The GeoJSON data as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r') as file:
        return json.load(file)

def write_geojson_to_generated_folder(
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
    with open(output_path, 'w') as file:
        json.dump(geojson_data, file, indent=2)
