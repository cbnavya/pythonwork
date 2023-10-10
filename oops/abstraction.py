#hiding implementation details
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def start():
        pass
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def accelerate():
        pass
class swift(car):
    def start(self):
        print("swift start")
    def stop(self):
        print("swift stop")
    def accelerate(self):
        print("swift accelerate")
obj=swift()
obj.start()
obj.accelerate()