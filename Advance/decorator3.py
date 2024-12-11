def error_handler(func_name):
    def wrapper(*args, **kwargs):
        print(" inside a decorator ")
        try:
            result = func_name(*args, **kwargs)
        except:
          
           return "some error occured"
        else:
           return result
        
    return wrapper
    
@error_handler
def divide(n1: int, n2: int):
    """function to divide two numbers."""
    return n1 / n2

print(divide(10, 2))  
print(divide(10, 0))


