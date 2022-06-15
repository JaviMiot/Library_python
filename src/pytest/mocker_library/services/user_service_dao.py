import typing
from abc import ABC, abstractmethod
from mocker_library.models import User


class UserServiceDao(ABC):
    @abstractmethod
    def get_all_users(self) -> typing.List[User]:
        pass

    @abstractmethod
    def create(self, data: dict) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, id: int) -> User:
        pass
