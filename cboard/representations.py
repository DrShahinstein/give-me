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


def create_json(path=JSON_PATH):
    with open(path, "w") as f:
        f.write("{}")


def create_new(representing_name, password):
    dir_exists = ROOT_DIR.exists()
    json_exists = JSON_PATH.exists()
    new_data = {representing_name: password, }

    if not dir_exists:
        os.mkdir(ROOT_DIR)
        create_json()

    if not json_exists:
        create_json()

    with open(JSON_PATH, "r+", encoding="utf-8") as f:
        content = json.load(f)
        content.update(new_data)
        f.seek(0)
        json.dump(content, f, indent=4)


def get(representing_name):
    with open(JSON_PATH, "r") as f:
        content = json.load(f)
        return content[representing_name]
