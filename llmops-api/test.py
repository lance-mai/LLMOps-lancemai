"""
@Time   : 2025/12/7 星期日 22:48
@Author : mailiangshi@gmail.com
@File   : test.py
"""
from injector import Injector, inject


class A:
    name: str = "mai"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"My Name is {self.a.name}")


injector = Injector()
b_instance = injector.create_object(B)
b_instance.print()
