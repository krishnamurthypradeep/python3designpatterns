import time
from enum import Enum

PizzaProgress = Enum("PizzaProgress","queued preparation baking ready")
PizzaDough = Enum("PizzaDough","thin thick")
PizzaSauce = Enum("PizzaSauce","tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping","mozzarella double_mozzarella red_onion oregano")

STEP_DELAY = 3

class Pizza:
    def __init__(self,name) -> None:
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
    def __str__(self) -> str:
        return self.name
    
    def prepare_dough(self,dough):
        self.dough = dough
        print(f"Preparing the {self.dough.name} ....")
        time.sleep(STEP_DELAY)
        print(f"Done with {self.dough.name} ....")  

# Two Builder MargaritaBuilder and PanneerBuilder

class MargaritaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    def add_sauce(self):
        print("adding tomato sauce to your margarita")
        self.pizza.sauce = PizzaSauce.tomato
        
        time.sleep(STEP_DELAY)
        print("done with tomato sauce")
    def add_topping(self):
        topping_desc ="double mozarella, oregano"
        topping_items = (PizzaTopping.double_mozzarella,PizzaTopping.oregano)
        
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f"done with the topping")
    def bake(self):
        self.progress = PizzaProgress.baking
        print(f"baking your margarita for {self.baking_time}")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("your margarita is ready")     
       
class PanneerBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza("panneer")
        self.progress = PizzaProgress.queued
        self.baking_time = 7
    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)
      
class Waiter:
    def __init__(self) -> None:
        self.builder = None
     
    def construct_pizza(self,builder):
        self.builder = builder
        steps =(builder.prepare_dough,builder.add_sauce,builder.add_topping,
                builder.bake) 
        [step() for step in steps]
    
    @property    
    def pizza(self):
        return self.builder.pizza   
   
   
def validate_style(builders):
    try:
        input_msg = "What pizza would you like [m]argarita or [p]anneer?"
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
    except KeyError:
        error_msg = "Sorry Only margarita (key m) and panneer (key p) available"
        print(error_msg)
        return (False,None)
    return (True,builder)

def main():
    builders = dict(m=MargaritaBuilder,p=PanneerBuilder)
    valid_input = False
    while not valid_input:
        valid_input , builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your pizza")  
    
main()                                              