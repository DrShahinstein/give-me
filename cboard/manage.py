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
from .utils import write_to_json, create_json, ROOT_DIR, JSON_PATH


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


def delete(representing_name):
    write_to_json(pop=representing_name)


def get(representing_name):
    with open(JSON_PATH, "r") as f:
        f_content = json.load(f)
        return f_content.get(representing_name, None)
