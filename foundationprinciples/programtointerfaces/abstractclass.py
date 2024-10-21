from abc import ABC,abstractmethod

class MyInterface(ABC):
    
    @abstractmethod
    def do_something(self,param: str):
        pass
    
class MyClass(MyInterface):
    def do_something(self,param: str):
        print(f"do something1 '{param}'")
        
if __name__ == "__main__":
    MyClass().do_something("some param")        
        
        