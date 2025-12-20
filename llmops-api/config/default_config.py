"""
@Time   : 2025/12/20 星期六 14:14
@Author : mailiangshi@gmail.com
@File   : default_config.py
"""

DEFAULT_CONFIG = {
    # wtf配置
    "WTF_CSRF_ENABLED": "FALSE",

    # SQLAlchemy数据库配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_ECHO": "TRUE",
    "SQLALCHEMY_POOL_SIZE": "30",
    "SQLALCHEMY_POOL_RECYCLE": "3600",
}
