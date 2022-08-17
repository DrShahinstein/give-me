import json
import os
from pathlib import Path

ROOT_DIR = Path(os.environ['HOME']) / ".representations"
JSON_PATH = ROOT_DIR / "index.json"


def write_to_json(new_data=None, pop=None, path=JSON_PATH):
    with open(path, "r+", encoding="UTF-8") as f:
        f_content_as_dict = json.load(f)

        if new_data is not None:
            f_content_as_dict.update(new_data)
        if pop is not None:
            print(f_content_as_dict.pop(pop, "Not Found"))

        f.seek(0)
        json.dump(f_content_as_dict, f, indent=4)


def create_json(path=JSON_PATH):
    with open(path, "w") as f:
        f.write("{}")


def hide(content):
    pass


def zip_json():
    with open(JSON_PATH, "r") as f: 
        f_content = json.load(f)
        keys = f_content.keys()
        values = f_content.values()
        return zip(keys, values)