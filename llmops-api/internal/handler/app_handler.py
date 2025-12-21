"""
@Time   : 2025/12/8 星期一 20:45
@Author : mailiangshi@gmail.com
@File   : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from internal.schema import CompletionReq
from internal.service import AppService
from pkg.response import success_json, validate_error_json, success_message, not_found_message

SYSTEM_PROMPT = "你是一个助手，请按照要求完成用户输入的指令。"


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        if not app:
            return not_found_message(f"the app {id} is not existed.")
        return success_message(f"app is deleted successfully, the deleted id is {app.id}")

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"app is created successfully, the id is {app.id}")

    def get_app(self, id: uuid.UUID):
        """调用服务查询APP记录"""
        app = self.app_service.get_app(id)
        return success_message(f"the name of app is {app.name}")

    def update_app(self, id: uuid.UUID):
        """调用服务更新APP记录"""
        app = self.app_service.update_app(id)
        return success_message(f"app is updated successfully, the new name is {app.name}")

    def ping(self):
        return success_message("On your service!")

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入 POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")

        # 2.构建OpenAI客户端，并发起请求
        llm = ChatOpenAI(model=os.getenv("MODEL"),
                         temperature=0.6,
                         api_key=os.getenv("API_KEY"),
                         base_url=os.getenv("BASE_URL"),
                         )
        parser = StrOutputParser()

        # 3.构建链
        chain = prompt | llm | parser

        # 4.调用链得到结果
        content = chain.invoke({"query": request.json.get("query")})

        return success_json(data={"content": content})
