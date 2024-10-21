import abc

class AbsFactory(abc.ABC):
    
    @abc.abstractmethod
    def create_economy():
        pass
    
    @abc.abstractmethod
    def create_suv():
        pass
    
    @abc.abstractmethod
    def create_luxury():
        pass