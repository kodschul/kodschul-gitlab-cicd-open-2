def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    
    return a / b

def power(base, exp):
    return base ** exp

def new_untested_func(a, b):
    return a + b - a + b


# version 1.0.1