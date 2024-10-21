# class Email:
#     def send_email(self,message):
#         print(f"Sending Email: {message}")
# class Notification:
#     def __init__(self) -> None:
#         self.email = Email()
#     def send(self,message):
#         self.email.send_email(message)

from typing import Protocol
class MessageSender(Protocol):
    def send(self,message: str):
        ...
 
class Email:
    def send(self,message):
        print(f"Sending Email: {message}")

class Notification:
    def __init__(self,sender: MessageSender) -> None:
        self.sender: MessageSender = sender
    def send(self,message):
        self.sender.send(message) 

if __name__ == "__main__":
    email = Email()
    notification= Notification(sender=email)
    notification.send(message = "Some Message")  
    
    
    
# GOF

#Creational : Aspects Of Object Creation     

# factory  pattern
# builder  pattern
 # Object pool
 # lazy Initialization
 # Dependency Injection (DI)  
 # Object Pool
 # Singleton vs Multiton       
                

        
                    