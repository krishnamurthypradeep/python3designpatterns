from importlib import import_module

def load_cust(cust_type):
    try:
        cust_module = import_module('.'+cust_type,'cust_objects')
    except ImportError:
        return None