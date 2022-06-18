from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Literal, Optional, Dict, TypedDict


class MessagesError(Enum):
    USER_NOT_FOUND = 'User not found'
    INVALID_PASSWORD = 'Invalid password'


class TypeCars(Enum):

    def _generate_next_value_(name, start, count, last_values):
        return f'THIS TYPE IS {name.upper()}'

    CAR = auto()
    TRUCK = auto()
    BUS = auto()


def show_error_message(type_error: MessagesError):
    print(type_error.value)


show_error_message(MessagesError.USER_NOT_FOUND)

print(MessagesError('User not found'))
# print(MessagesError('User invalid'))
print(list(TypeCars))

cars_types: Literal['Béchamel', 'Velouté', 'Espagnole',
                    'Tomato', 'Hollandaise'] = 'Hollandaise'

cars: TypeCars = TypeCars.TRUCK

"""
Literals in python
this define type by position in a array
"""
sauce: Literal['Béchamel', 'Velouté', 'Espagnole',
               'Tomato', 'Hollandaise'] = 'Hollandaise'


@dataclass()
class Address:
    name: str


@dataclass()
class Car:
    type: TypeCars
    name: str


class CarInfo(TypedDict):
    user_name: str
    car: Car
    address: Address


ListCars = List[CarInfo]

cars_and_address: ListCars = []

cars_and_address.append(
    CarInfo(
        user_name='javier',
        car=Car(
            type=TypeCars.BUS,
            name='chuchu'
        ),
        address=Address('pifo')
    )
)

cars_and_address.append(
    CarInfo(
        user_name='jose',
        car=Car(
            type=TypeCars.TRUCK,
            name='peter'
        ),
        address=Address('d')
    )
)

print(cars_and_address[0])
