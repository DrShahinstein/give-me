import json


def load_passwords(file_path):
    try:
        with file_path.open("rb") as f:
            return json.loads(f.read().decode())
    except FileNotFoundError:
        return {}


def save_passwords(file_path, data):
    with file_path.open("wb") as f:
        f.write(json.dumps(data).encode())
