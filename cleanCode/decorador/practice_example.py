from dataclasses import dataclass


class Serializer:

    def serialize(self, event):
        return {
            'name': event.name,
            'email': event.email,
            'password': 'hide password',
            'address': event.address.upper()
        }


@dataclass
class Log_Event:
    name: str
    email: str
    password: str
    address: str

    def serializer(self, serializer: Serializer):
        return serializer.serialize(self)


logEvent = Log_Event('javier', 'javi@mail.com', 'erer3434', 'pifo')
print(logEvent.serializer(Serializer()))
