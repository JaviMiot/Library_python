import typing
from dataclasses import dataclass


@dataclass()
class User:
    id: typing.Union[int, str]
    name: str
    lastname: str