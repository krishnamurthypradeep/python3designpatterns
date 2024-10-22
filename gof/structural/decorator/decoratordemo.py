import functools
def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def memoizer(*args):
        if args not in cache:
            cache[args] = func(*args)
            
        return cache[args]
    return memoizer

@memoize
def number_sum(n):
    if n == 0:
        return 0
    else:
        return n+number_sum(n-1) 

@memoize    
def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
    
def main():
    from timeit import Timer
    to_execute =[
        (
            number_sum,
            Timer(
                "number_sum(300)",
                "from __main__ import number_sum",
            ),
        ),
        (
            fibonacci,
            Timer(
                "fibonacci(100)",
                "from __main__ import fibonacci"
            ),
        ),
    ]    
    for item in to_execute:
        func = item[0]
        print(f'Function "{func.__name__}":{func.__doc__}')
        t = item[1]
        print(f"Time: {t.timeit()}")
        print()  
      
if __name__ == "__main__":
    main()           
        
class Memoize:
    def __init__(self,func) -> None:
        self.func = func
    def __call__(self, *args: functools.Any, **kwds: functools.Any) -> functools.Any:
        if args not in cache:
            cache[args] = func(*args)
            
        return cache[args]
                   