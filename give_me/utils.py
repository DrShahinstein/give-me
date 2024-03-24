import json
import os
from pathlib import Path


ROOT_DIR = Path(os.environ['HOME']) / ".config" / ".passwords"
JSON_PATH = ROOT_DIR / "index.json"


def init_json(func):
    def wrapper():
        dir_exists = ROOT_DIR.exists()
        json_exists = JSON_PATH.exists()

        if not dir_exists:
            os.mkdir(ROOT_DIR)
            create_json()

        if not json_exists:
            create_json()

        func()
    return wrapper

def write_to_json(new_data, path=JSON_PATH):
    json_content = get_dict_from_json()
    json_content.update(new_data)
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(json_content, f, indent=4)


def create_json(path=JSON_PATH):
    with open(path, "w") as f:
        f.write("{}")


def get_dict_from_json(path=JSON_PATH):
    with open(path, "r") as f:
        return json.load(f)


def zip_json():
    json_content = get_dict_from_json()
    keys = json_content.keys()
    values = json_content.values()
    return zip(keys, values)


# Checks whether a zip object is empty or not.
def is_empty(zip):
    try:
        next(zip)
        return False
    except StopIteration:
        return True
