"""
@Time   : 2025/12/8 星期一 21:41
@Author : mailiangshi@gmail.com
@File   : Http.py
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from internal.exception import CustomerException
from internal.router import Router
from pkg.response import Response, json, HttpCode


class Http(Flask):
    """http服务引擎"""

    def __init__(self, *args, config: Config, db: SQLAlchemy, router: Router, **kwargs):
        # 调用父类构造方法
        super().__init__(*args, **kwargs)

        # 加载应用配置
        self.config.from_object(config)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化Flask扩展
        db.init_app(self)

        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        # 1.异常信息如果时自定义异常，则返回自定义异常信息
        if isinstance(error, CustomerException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))
        # 2.如果不是自定义异常，则返回系统异常信息
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error  # 方便调试
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={},
            ))
