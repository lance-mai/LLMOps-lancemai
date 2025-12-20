"""
@Time   : 2025/12/20 星期六 17:36
@Author : mailiangshi@gmail.com
@File   : sqlalchemy.py
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):
    """重写SQLAlchemy，添加自动提交功能"""

    @contextmanager
    def auto_commit(self):
        try:
            yield  # 这里的yield就是进入到with代码块中，然后执行代码块中的代码
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
