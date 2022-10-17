"""
Json example
{
    "[representing_name]": "[something_to_copy]",
    "ghtoken": "ghpLJOPSjkGLugnlsou>KjKlmljh>"
    ...
}
"""


import os
from .utils import pop, get_dict_from_json, write_to_json, create_json, ROOT_DIR, JSON_PATH


def create_new(representing_name, content):
    dir_exists = ROOT_DIR.exists()
    json_exists = JSON_PATH.exists()
    pair = {representing_name: content, }

    if not dir_exists:
        os.mkdir(ROOT_DIR)
        create_json()

    if not json_exists:
        create_json()

    write_to_json(pair)


def delete(representing_name):
    pop(representing_name)


def get(representing_name):
    json_content = get_dict_from_json()
    return json_content.get(representing_name, None)
