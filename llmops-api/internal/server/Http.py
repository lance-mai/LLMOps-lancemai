"""
@Time   : 2025/12/8 星期一 21:41
@Author : mailiangshi@gmail.com
@File   : Http.py
"""

from flask import Flask

from config import Config
from internal.router import Router


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, config: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)

        # 加载应用配置
        self.config.from_object(config)
