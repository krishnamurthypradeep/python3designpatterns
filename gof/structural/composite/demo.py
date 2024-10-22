import abc
from collections.abc import Iterable
from functools import reduce
from datetime import date
from typing import Iterator
from dateutil.relativedelta import relativedelta
class AbsComposite(abc.ABC):
    
    @abc.abstractmethod
    def get_oldest(self):
        pass
    
class Person(AbsComposite):
    def __init__(self,name,birthdate) -> None:
        self._name = name
        self._birthdate = birthdate
        
    def get_oldest(self):
        return self
    
    @property
    def name(self):
        return self._name  
    
    @property
    def birthdate(self):
        return self._birthdate
class NullPerson(AbsComposite):
    name = None
    birthdate = date.max
        
    def get_oldest(self):
        return self
        

class Tree(Iterable, AbsComposite):
    def __init__(self,members) -> None:
        self.members = members
    
    def __iter__(self) -> Iterator:
        return iter(self.members)
    
    def get_oldest(self):
        def f(t1,t2):
            t1_, t2_ =t1.get_oldest(),t2.get_oldest()
            return t1_ if t1_.birthdate < t2_.birthdate else t2_
        return reduce(f,self,NullPerson())
  
def main():
    persons1 = Tree([
        Person('Person1',date(1970,3,14)),
        Person('Person2',date(1965,7,4)),
        Person('Person3',date(1995,2,2)),
        Person('Person4',date(1997,5,1)),
        Person('Person5',date(1999,4,2)),
    ])  
    
    persons2 = Tree([
        Person('Person6',date(1991,1,1)),
        Person('Person7',date(1993,9,9)),
    ])
    person = Person('SinglePerson',date(1990,6,6))  
    
    tree1 = Tree([persons1])
    tree2 = Tree([persons2,person])
    tree3 = Tree([persons1,persons2])
    
    for tree in tree1,tree2,tree3:
        oldest = tree.get_oldest()
        age= relativedelta(date.today(),oldest.birthdate)
        print(f'Oldest Person: {oldest.name}; Age {age.years}, {age.months} months')
    
    
if __name__ == "__main__":
    main()            
                    