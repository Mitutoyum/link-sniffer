import json

from core.config import config_path
from typing import Any


def load_config() -> dict:
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    return config


def get_flag(
    path: str,
    default: Any = None,
):
    path_list = path.split(".")
    config = load_config()

    for i in path_list:
        try:
            config = config[i]
        except KeyError:
            return default

    return config
