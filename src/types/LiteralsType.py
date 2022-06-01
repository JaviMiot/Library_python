from typing import Literal

Data = Literal['a', 'b', 'c']


def func(data: Data) -> None:
    pass


func('a1')
