from random import randint


class Sensor_dummy():
    def __init__(self, value_range: list[int]) -> None:
        self.value_range: list[int] = value_range
        self.value = randint(self.value_range[0], self.value_range[1])

    def getValue(self) -> float:
        self.value += 1
        return self.value
