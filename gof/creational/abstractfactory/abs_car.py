import abc
class AbsCar(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass
    
    @abc.abstractmethod
    def stop(self):
        pass