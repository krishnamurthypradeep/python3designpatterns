from abs_factory import AbsFactory
from gm.chevrolet import GMChevrolet
class GMFactory(AbsFactory):
    
    @staticmethod
    def create_economy():
        return GMChevrolet()
    
    @staticmethod
    def create_suv():
        return GMChevrolet()
    
    @staticmethod
    def create_luxury():
        return GMChevrolet()