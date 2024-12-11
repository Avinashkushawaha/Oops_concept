def int_type_checker(func_name):

    def wrapper (*args, **kwargs):
        print('inside a decorator')
        
        int_type = all(isinstance(value, int) for value in  args)   

        int_type &= all(isinstance(value, int) for value in kwargs.values()) 
        
        
        if int_type:
            return func_name(*args, **kwargs)
        else:  
            return "invalid values can not executes"
    return wrapper  

@int_type_checker
def add(n1:int, n2=int):
    return n1 + n2
print(add(10, 20))
print(add(10, "20"))
print(add(10, n2=30))
print(add(10, n2="next"))      
            

     
        