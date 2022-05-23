class DecodeUrl:
    def decode(self, data: str, separator: str):
        return data.split(separator)


data = 'javie-manobanda-turori'
decodeUrl = DecodeUrl()
print(decodeUrl.decode(data, '-'))


class DecodeMixin:
    def decode(self, data: str, separator: str):
        return list(map(lambda data: data.upper(), super().decode(data, separator)))


class DecodeUpperCase(DecodeMixin, DecodeUrl):
    pass


decodeMixin = DecodeUpperCase()
print(decodeMixin.decode(data, '-'))
