"""
@Time   : 2025/12/20 星期六 15:32
@Author : mailiangshi@gmail.com
@File   : app_service.py
"""
import uuid
from dataclasses import dataclass
from uuid import uuid4

from injector import inject

from internal.model import App
from pkg.sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        """
        db.auto_commit()方法中的yield是上下文管理器（contextmanager） 结合生成器的典型用法，它的作用是标记 with
        代码块的执行边界—— 程序执行到yield时会暂时跳出auto_commit方法，
        去执行with self.db.auto_commit():下面的所有业务代码，等业务代码执行完后，
        再回到yield的下一行继续执行提交 / 回滚逻辑
        """
        with self.db.auto_commit():
            # 1.创建模型的实体类
            app = App(name="聊天机器人", icon="", description="这是一个简单的聊天机器人", account_id=uuid4())
            # 2.将实体类添加到session会话中
            self.db.session.add(app)
            # 3.提交会话以及错误时回滚，这个是在db.auto_commit()中操作的
        return app

    def get_app(self, id: uuid.UUID) -> App:
        return self.db.session.query(App).get(id)

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "麦兜机器狗"
        return app

    def delete_app(self, id: uuid.UUID) -> App | None:
        with self.db.auto_commit():
            app = self.get_app(id)
            if not app:
                return None
            self.db.session.delete(app)
        return app
