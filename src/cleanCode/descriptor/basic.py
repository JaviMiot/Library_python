
import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')


# class Attribute:
#     value = 2


# class Client:
#     attribute = Attribute()


# print(Client().attribute)
# print(Client().attribute.value)


class DescriptorClass:

    def __get__(self, instance, owner):
        """_summary_

        Args:
            instance (_type_): refer to the object that was called (in this case is client)
            owner (_type_): this a reference to the class of that object (in this case is ClientClass).

        Returns:
            _type_: _description_
        """
        if instance is None:
            return f'{self.__class__.__name__}.{owner.__name__}'

        return f'value for {instance}'

    def __set__(self, instance, value):
        """is called when assign something to the description

        Args:
            instance (_type_): in this case can be the client
            value (_type_): some value as 'string'
        """
        pass


class ClientClass:
    descriptor = DescriptorClass()


client = ClientClass()

print('is called from instance')
print(client.descriptor)
print(ClientClass().descriptor)
print('is called from the class')
print(ClientClass.descriptor)
print('using set method')
client.descriptor = 'value'
