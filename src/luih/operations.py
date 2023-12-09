from time import sleep
from luih.utils import get_cwd


def a_add_two_numbers(a: int, b: int) -> int:
    sleep(5)
    return a + b


def _multiply_two_numbers(a: int, b: int) -> int:
    get_cwd()
    return a * b


def _divide_two_numbers(a: int, b: int) -> float:
    return a / b
