from data_sink.sinkInterface import DataSink
import time
import datetime

class CsvWriter(DataSink):
    def __init__(self, directory: str, maxWriteCount: int) -> None:
        self.directory = directory
        self.counter = 0
        self.filename = self._getFilename()
        self.maxWriteCount = maxWriteCount

    def _getFilename(self) -> str:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = self.directory + 'data_' + timestr + '.csv'
        return filename

    def writeData(self, data: list[str]) -> None:
        self.counter += 1
        if self.counter > self.maxWriteCount:
                self.filename = self._getFilename()
                self.counter = 0
        with open(self.filename,'a') as file:
            currentTime = str(datetime.datetime.now())
            print_str = currentTime + ","
            for element in data:
                print_str += element + ","

            file.write(print_str + "\n")
