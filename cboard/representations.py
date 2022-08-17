"""
Json example
{
    "[representing_name]": "[something_to_copy]",
    "ghtoken": "ghpLJOPŞjkGLugnlşou>KjKlmljh>"
    ...
}
"""

import json
import os
from pathlib import Path

ROOT_DIR = Path(os.environ['HOME']) / ".representations"
JSON_PATH = ROOT_DIR / "index.json"


def create_new(representing_name, content):
    dir_exists = ROOT_DIR.exists()
    json_exists = JSON_PATH.exists()
    new_representation = {representing_name: content, }

    if not dir_exists:
        os.mkdir(ROOT_DIR)
        create_json()

    if not json_exists:
        create_json()

    write_to_json(new_representation)


def remove(representing_name):
    write_to_json(pop=representing_name)


def get(representing_name):
    with open(JSON_PATH, "r") as f:
        content = json.load(f)
        return content[representing_name]


def write_to_json(new_representation=None, pop=None, path=JSON_PATH):
    with open(path, "r+", encoding="UTF-8") as f:
        f_content_as_dict = json.load(f)

        if new_representation is not None:
            f_content_as_dict.update(new_representation)
        if pop is not None:
            print(f_content_as_dict.pop(pop, "Not Found"))

        f.seek(0)
        json.dump(f_content_as_dict, f, indent=4)


def create_json(path=JSON_PATH):
    with open(path, "w") as f:
        f.write("{}")
