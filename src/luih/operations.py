from time import sleep
from luih.utils import get_cwd


def add_two_numbers(a: int, b: int) -> int:
    sleep(5)
    return a + b


def multiply_two_numbers(a: int, b: int) -> int:
    get_cwd()
    return a * b


def divide_two_numbers(a: int, b: int) -> float:
    return a / b
