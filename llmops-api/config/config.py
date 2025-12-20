"""
@Time   : 2025/12/11 星期四 21:53
@Author : mailiangshi@gmail.com
@File   : config.py
"""
import os
from typing import Any

from .default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    """从环境变量中获取配置项，找不到则返回默认配置"""
    return os.getenv(key, DEFAULT_CONFIG)


def _get_bool_env(key: str) -> bool:
    """从环境变量中获取布尔值配置项，找不到则返回默认配置"""
    value: str = _get_env(key)
    return value.lower() == "true" if value else False


class Config:
    """系统配置"""

    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = _get_env("WTF_CSRF_ENABLED")

        # 数据库配置
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
