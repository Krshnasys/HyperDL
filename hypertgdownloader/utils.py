import os
from pathlib import Path

def ensure_directory_exists(directory: str):
    Path(directory).mkdir(parents=True, exist_ok=True)

def get_temp_part_path(directory, filename, idx):
    return os.path.join(directory, f"{filename}.part{idx:02d}")