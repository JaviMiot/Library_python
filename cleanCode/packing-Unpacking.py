import re


USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(1_000)]


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'User({self.first_name}, {self.last_name})'


user1 = User(1, 'javie', 'manobanda')
print(repr(user1))
