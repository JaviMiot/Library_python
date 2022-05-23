def format(fn):
    def wrapper(data):
        return fn(data).upper()
    return wrapper


def format_with_parameters(precondition: str = ''):
    def get_function(fn):
        def wrapper(data):
            return f'{precondition} {fn(data).upper()}'
        return wrapper
    return get_function


def format_with_parameters_postcondition(postcondition: str = ''):
    def get_function(fn):
        def wrapper(data):
            return f'{fn(data).upper()} {postcondition}'
        return wrapper
    return get_function


def say_name(name: str):
    return name


@format
def say_name2(name: str):
    return name


@format_with_parameters('your name is:')
@format_with_parameters_postcondition('Hi all!')
def say_name3(name: str):
    return name


say_name_uppercase = format(say_name)
print(say_name_uppercase('hola'))

print(say_name2('jorge'))

print(say_name3('jenny'))
