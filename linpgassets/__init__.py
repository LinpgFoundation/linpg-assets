from json import load as JSON_LOAD
from os import path as PATH
from typing import Final

# 引擎素材路径
__LINPG_INTERNAL_IMAGE_PATH: Final[str] = PATH.join(PATH.dirname(__file__), "image")


# 获取引擎素材路径
def get_image_location() -> str:
    return __LINPG_INTERNAL_IMAGE_PATH


# 获取数据库路径
def get_database_path() -> str:
    return PATH.join(PATH.dirname(__file__), "config", "database.json")


# 获取数据库
def get_database() -> dict[str, dict[str, dict[str, bool]]]:
    with open(get_database_path(), "r", encoding="utf-8") as f:
        return dict(JSON_LOAD(f))
