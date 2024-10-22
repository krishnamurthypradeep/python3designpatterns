from enum import Enum
from abc import ABC,abstractmethod

State = Enum("State","NEW RUNNING SLEEPING")
class User:
    pass
class Process:
    pass
class File:
    pass


class Server(ABC):
    @abstractmethod
    def __init__(self) -> None:
       pass
    def __str__(self) -> str:
        return self.name
    
    @abstractmethod
    def boot(self):
        pass  
    
    @abstractmethod
    def kill(self,restart=True):
        pass 
    
class FileServer(Server):
    def __init__(self) -> None:
       self.name = "FileServer"
       
   
    
    
    def boot(self):
        print(f"booting the {self}")
        self.state = State.RUNNING
    
    
    def kill(self,restart=True):
        print(f"killing {self}")
        self.state = State.RESTART if restart else State.RUNNING
     
class ProcessServer(Server):
    def __init__(self) -> None:
       self.name = "ProcessServer"
       
   
    
    
    def boot(self):
        print(f"booting the {self}")
        self.state = State.RUNNING
    
    
    def kill(self,restart=True):
        print(f"killing {self}")
        self.state = State.RESTART if restart else State.RUNNING        

class OperatingSystem:
    def __init__(self) -> None:
       self.fs = FileServer()
       self.ps - ProcessServer()
    
    def start(self):
        [i.boot() for i in (self.fs, self.ps)]
           
        
        
        
     
   