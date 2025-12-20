"""
@Time   : 2025/12/20 星期六 12:03
@Author : mailiangshi@gmail.com
@File   : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomerException(Exception):
    """基础自定义异常信息"""
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomerException):
    """失败异常信息"""
    pass


class NotFoundException(CustomerException):
    """未找到异常信息"""
    code = HttpCode.NOT_FOUND


class UnauthorizedException(CustomerException):
    """未授权异常信息"""
    code = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomerException):
    """无授权异常信息"""
    code = HttpCode.FORBIDDEN


class ValidateException(CustomerException):
    """数据验证异常信息"""
    code = HttpCode.VALIDATE_ERROR
