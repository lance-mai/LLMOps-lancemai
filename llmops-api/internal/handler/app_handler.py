"""
@Time   : 2025/12/8 星期一 20:45
@Author : mailiangshi@gmail.com
@File   : app_handler.py
"""
import os

from flask import request
from openai import OpenAI

from internal.schema import CompletionReq

SYSTEM_PROMPT = "你是一个助手，请按照要求完成用户输入的指令。"


class AppHandler:
    """应用控制器"""

    def ping(self):
        return {"ping": "pong"}

    def completion(self):
        """聊天接口"""
        # 1.提取从接口中获取的输入 POST
        req = CompletionReq()
        if not req.validate():
            return req.errors
        query = request.json.get("query")

        # 2.构建OpenAI客户端，并发起请求
        client = OpenAI(
            api_key=os.getenv("API_KEY"),
            base_url=os.getenv("BASE_URL"),
        )

        # 3.获得响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query}
            ],
            temperature=0.6,
        )

        content = completion.choices[0].message.content
        return content
