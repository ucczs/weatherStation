import datetime
from data_sink.sinkInterface import DataSink

class consoleWriter(DataSink):
    def __init__(self) -> None:
        pass

    def writeData(self, data: list[str]) -> None:
        print_str = str(datetime.datetime.now()) + ", "
        for element in data:
            print_str += element + ", "
        print(print_str[:-2])
