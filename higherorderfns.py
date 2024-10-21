def f(x):
    return x+2

def g(fn,x):
    return fn(x) * 2

print(g(f,42))

# Closure
def addx(x):
    def _(y):
        return x+y
    return _
print(addx(2)(4))

def f(x,y):
    return x*y

def f2(x):
    def _(y):
        return f(x,y)
    return _

print(f2(2)(3))
# currying

