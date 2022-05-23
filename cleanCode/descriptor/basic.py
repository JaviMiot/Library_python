
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')


class Attribute:
    value = 2


class Client:
    attribute = Attribute()


print(Client().attribute)
print(Client().attribute.value)


class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        logging.info(f'call: {self.__class__.__name__} {instance} {owner}')

        return instance


class ClientClass:
    descriptor = DescriptorClass()


client = ClientClass()
client.descriptor
print(client.descriptor is client)
DescriptorClass()
