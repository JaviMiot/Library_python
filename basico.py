from typing import List, Tuple


def get_data(data: int) -> int:
    return data


my_list: List[int] = [1, 2, 3, 3, 4]

get_data(1)


Color = Tuple[int, int, int]


def set_rgb(color: Color) -> None:
    pass


set_rgb((1, 2, 3))
