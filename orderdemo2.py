class Order:
    # class attributes
    orders = []
    # instance attributes
    orderid: int = 0
    shipping_address: str = ''
    shipped: bool = False
    expedited: bool = False
    shipped: bool = False
    customer: object = None
    
    @staticmethod
    def process_expedited(order):
        return order.expedited
    
    @staticmethod
    def process_not_expedited(order):
        return not order.expedited
    
    @staticmethod
    def get_customer_name(order):
        return order.customer.name
    
    # instance methods
    @staticmethod
    def get_filtered_info(predicate,func):
        output = []
        for order in Order.orders:
            if predicate(order):
                output.append(func(order))
        return output
    
    @staticmethod
    def get_expedited_orders_customer_names():
        return Order.get_filtered_info(Order.process_expedited,Order.get_customer_name)
    
     
    @staticmethod
    def get_expedited_orders_customer_addresses():
        output = []
        for order in Order.orders:
            if order.expedited:
                output.append(order.customer.address)
        return output
    
    @staticmethod
    def get_expedited_orders_shipping_addresses():
        output = []
        for order in Order.orders:
            if order.expedited:
                output.append(order.shipping_address)
        return output        
    
    # Higher Order Functions
    
    # software design principles and  SOLID
     # Maintainable
     # Scalable
     # Robust
     
     # Four Foundation Principles
     # 1. Encapsulate What Varies
     # 2. Favor Composition Over Inheritance
     # 3. Program To Interfaces
     # 4. Loose Coupling
     
     # SOLID Principles
     # GOF Patterns
     
     # Requirements Evolve
     # Technologies Advance
     # User needs also Change
     
     