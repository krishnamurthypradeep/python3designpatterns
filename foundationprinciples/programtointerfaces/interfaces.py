from abc import ABC,abstractmethod

class Logger(ABC):
    
    @abstractmethod
    def log(self,message: str):
        pass
    
class ConsoleLogger(Logger):
    def log(self,message: str):
        print(f"Console '{message}'")

class FileLogger(Logger):
    def log(self,message: str):
        with open("log.txt","a") as f:
            f.write(f"File: {message}\n")
                

def log_message(logger: Logger,message: str):
    logger.log(message)        
if __name__ == "__main__":
    log_message(ConsoleLogger(),"A Console Log")
    log_message(FileLogger(),"A File Log")        
        
      
      # SOLID
      # S -> Single Responsiblity Principle
      # O -> Open Closed Principle
      # L -> LiskOV substitution Principle
      # I -> Interface Segregation Principle
      # D -> Dependency Inversion Principle
      
      # Microservices Architecture
        