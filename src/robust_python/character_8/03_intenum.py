from enum import IntEnum


class ImperialLiquidMeasure(IntEnum):
    CUP = 8
    PINT = 16
    QUART = 32
    GALLON = 128


print(ImperialLiquidMeasure.CUP == 8)
