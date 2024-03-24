"""
Json example
{
    "[name]": "[something_to_copy]",
    "ghtoken": "ghpLJOPSjkGLugnlsou>KjKlmljh>"
    ...
}
"""


import json
from .utils import get_dict_from_json, JSON_PATH


class Password:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get(name):
        json_content = get_dict_from_json()
        return json_content.get(name, None)

    @staticmethod
    def pop(password, path=JSON_PATH):
        json_content = get_dict_from_json()
        json_content.pop(password)
        with open(path, "w", encoding="UTF-8") as f:
            json.dump(json_content, f, indent=4)

    @staticmethod
    def hide(content: str):
        space = ' '
        return "".join(list(map(lambda char: '*' if not char == space else space, content)))
