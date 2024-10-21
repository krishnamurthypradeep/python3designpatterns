from .abs_factory import AbsFactory
from .ford.fiesta import FordFiesta
class FordFactory(AbsFactory):
    
    @staticmethod
    def create_economy():
        return FordFiesta()
    
    @staticmethod
    def create_suv():
        return FordFiesta()
    
    @staticmethod
    def create_luxury():
        return FordFiesta()