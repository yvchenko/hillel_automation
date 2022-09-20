import json
from pathlib import Path


full_path = Path(__file__)

root_path = full_path.parent.parent

file_name = "resources/data.json"
resources_folder = "resources"

file_path = root_path.joinpath(resources_folder, file_name)

print(file_path)

