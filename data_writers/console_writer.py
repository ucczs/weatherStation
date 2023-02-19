import datetime
from data_writers.writerInterface import DataWriter

class consoleWriter(DataWriter):
    def __init__(self) -> None:
        pass

    def writeData(self, data: list[str]) -> None:
        print_str = str(datetime.datetime.now()) + ", "
        for element in data:
            print_str += element + ", "
        print(print_str[:-2])
