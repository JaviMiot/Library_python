class Format:

    def __init__(self, data):
        self.data = data

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            return f'{self.data} {fn(*args, **kwargs).upper()}'

        return wrapper


@Format('como estas')
def say_name2(name: str):
    return name


print(say_name2('jorge'))
