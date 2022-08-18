import json
import os
from pathlib import Path

ROOT_DIR = Path(os.environ['HOME']) / ".representations"
JSON_PATH = ROOT_DIR / "index.json"


def write_to_json(new_data, path=JSON_PATH):
    json_content = get_dict_from_json()
    json_content.update(new_data)
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(json_content, f, indent=4)


def pop(representing_name, path=JSON_PATH):
    json_content = get_dict_from_json()
    json_content.pop(representing_name)
    with open(path, "w", encoding="UTF-8") as f:
        json.dump(json_content, f, indent=4)


def create_json(path=JSON_PATH):
    with open(path, "w") as f:
        f.write("{}")


def get_dict_from_json(path=JSON_PATH):
    with open(path, "r") as f:
        return json.load(f)


def hide(content: str):
    space = ' '
    return "".join(list(map(lambda char: '*' if not char == space else space, content)))


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
