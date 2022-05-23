class Suma:
    def __init__(self, sumador: int):
        self.sumador = sumador

    def __call__(self, number: int):
        return self.sumador + number


su = Suma(3)
print(su(3))
print(su(5))
print(su(2))
print(su(1))
