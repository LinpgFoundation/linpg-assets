from os import path as PATH
from typing import Final

# 引擎素材路径
__LINPG_INTERNAL_IMAGE_PATH: Final[str] = PATH.join(PATH.dirname(__file__), "image")


# 获取引擎素材路径
def get_image_location() -> str:
    return __LINPG_INTERNAL_IMAGE_PATH


# 数据库路径
__DATABASE_PATH: Final[str] = PATH.join(
    PATH.dirname(__file__), "config", "database.json"
)


# 获取数据库路径
def get_database_path() -> str:
    return __DATABASE_PATH
