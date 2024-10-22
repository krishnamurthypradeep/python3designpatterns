class OldPaymentSystem:
    def __init__(self,currency) -> None:
        self.currency = currency
    def make_payment(self,amount):
        print(f"[OLD] Pay {amount} {self.currency}")
        
class NewPaymentSystem:
    def __init__(self,currency) -> None:
        self.currency = currency
    def execute_payment(self,amount):
        print(f"[OLD] Pay {amount} {self.currency}")  

class PaymentGateway:
    def __init__(self,currency) -> None:
        self.currency = currency
    
    def execute_payment(self,amount):
        print(f"[OLD] Pay {amount} {self.currency}") 
     
class PaymentAdapter:
    def __init__(self,system) -> None:
        self.system  = system
    def make_payment(self,amount):
        self.system.execute_payment(amount)  

def main():
    old_system = OldPaymentSystem("INR")
    print(old_system)
    new_system = PaymentGateway("INR")
    print(new_system)
    adapter = PaymentAdapter(new_system)
    adapter.make_payment(1000)          
                
                      
        
if __name__ == "__main__":
    main()             
    
# Composite Pattern

# when your data fits as tree like structure
# Client code can treat the data uniformly
# We will   adhere to Open Closed Principles
# but we will violate SRP  