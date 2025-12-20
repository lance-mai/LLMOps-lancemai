"""
@Time   : 2025/12/20 星期六 15:32
@Author : mailiangshi@gmail.com
@File   : app_service.py
"""
import uuid
from dataclasses import dataclass
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self) -> App:
        # 1.创建模型的实体类
        app = App(name="聊天机器人", icon="", description="这是一个简单的聊天机器人", account_id=uuid4())
        # 2.将实体类添加到session会话中
        self.db.session.add(app)
        # 3.commit
        self.db.session.commit()
        return app

    def get_app(self, id: uuid.UUID) -> App:
        return self.db.session.query(App).get(id)

    def update_app(self, id: uuid.UUID) -> App:
        app = self.get_app(id)
        app.name = "麦兜机器狗"
        self.db.session.commit()
        return app

    def delete_app(self, id: uuid.UUID) -> App | None:
        app = self.get_app(id)
        if not app:
            return None
        self.db.session.delete(app)
        self.db.session.commit()
        return app
