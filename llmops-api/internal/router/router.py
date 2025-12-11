"""
@Time   : 2025/12/8 星期一 20:51
@Author : mailiangshi@gmail.com
@File   : router.py
"""

from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1.创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2.将url与对应的控制器方法做绑定
        # app_handler = AppHandler()
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)

        # 3.将蓝图注册到app中
        app.register_blueprint(bp)
