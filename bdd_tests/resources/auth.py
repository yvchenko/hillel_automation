import json
from os.path import join, dirname


def get_credentials(auth_file):
    """
    Parses the json file with credentials and turns them into a tuple
    """
    file = _load_credentials(auth_file)
    with open(file, "r") as file:
        data = json.load(file)
        credentials = (data["name"], data["password"])
    return credentials


def _load_credentials(filename):
    """
    Loads the credentials file
    """
    relative_path = join('', filename)
    absolute_path = join(dirname(__file__), relative_path)
    return absolute_path
