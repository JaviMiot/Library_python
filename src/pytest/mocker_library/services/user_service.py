import typing
from faker import Faker

from mocker_library.services.user_service_dao import UserServiceDao
from mocker_library.models import User

faker = Faker()


class UserService():
    def __init__(self, user_service: UserServiceDao):
        self.user_service = user_service

    def get_all_users(self):
        return self.user_service.get_all_users()

    def create(self, data: dict) -> User:
        return self.user_service.create(data)

    def get_user_by_id(self, id: int) -> User:
        return self.user_service.get_user_by_id(id)
