import typing
from faker import Faker

from mocker_library.services.user_service_dao import UserServiceDao
from mocker_library.models import User

faker = Faker()


class UserServiceLocal(UserServiceDao):
    def __init__(self):
        self._users: typing.List[User]
        self._generate_users()

    def _generate_users(self):
        self._users = [User(id, faker.name(), faker.name())
                       for id in range(20)]

    def get_all_users(self):
        return self._users

    def create(self, data: dict) -> User:
        id = len(self._users)
        data['id'] = id
        new_user = User(**data)
        self._users.append(new_user)
        return self.get_user_by_id(id)

    def get_user_by_id(self, id: int) -> User:
        return self._users[id]
