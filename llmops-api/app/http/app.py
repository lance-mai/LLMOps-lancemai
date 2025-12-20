"""
@Time   : 2025/12/8 星期一 21:50
@Author : mailiangshi@gmail.com
@File   : app.py
"""

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from app.http.module import ExtensionModule
from config import Config
from internal.router import Router
from internal.server import Http

# 从.env文件中加载环境变量
dotenv = load_dotenv()

config = Config()

injector = Injector([ExtensionModule])
app = Http(__name__, config=config, db=injector.get(SQLAlchemy), router=injector.get(Router))

# 只有当这个文件被直接运行时，才会执行下面的代码
if __name__ == "__main__":
    app.run(debug=True, port=5000)
