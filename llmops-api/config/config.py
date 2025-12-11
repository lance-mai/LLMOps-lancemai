"""
@Time   : 2025/12/11 星期四 21:53
@Author : mailiangshi@gmail.com
@File   : config.py
"""


class Config:
    """系统配置"""

    def __init__(self):
        # 关闭wtf的csrf保护
        self.WTF_CSRF_ENABLED = False
