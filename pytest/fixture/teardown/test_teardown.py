import pytest
import time


class Dog:
    def ladrar(self):
        time.sleep(1)
        return 'ladrar'

    def dormir(self):
        return 'dormir'


@pytest.fixture
def get_dog():
    dog = Dog()
    status = dog.ladrar()
    yield status
    print(dog.dormir())


def test_dog(get_dog):
    ladrar = get_dog
    assert ladrar == 'ladrar'
