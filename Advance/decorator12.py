class Math:
    def __init__(self,n1, n2):
        self.n1 = n1
        self.n2 = n2
    def add(self):
        return self.n1 + self.n2
    def divide(self):
        return self.n1/self.n2
    def multiply(self):
        return self.n1 * self.n2

def class_deco(cls_name):
    def method_decoration(method_name):
        def wrapper(*args,**kwargs):
            print(f'Executing{method_name.__name__}')
            result = method_name(*args, **kwargs)
            print(f'Result: {result}')
            return result
        return wrapper
    
    for attr in dir(cls_name):
        if callable(getattr(cls_name, attr)) and not attr.startswith("__"):
            method = getattr(cls_name, attr)
            decorated_method = method_decoration(method)
            setattr(cls_name, attr, decorated_method)
    return cls_name

@class_deco
class Math:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2
    
    def divide(self):
        if self.n2 != 0:
            return self.n1 / self.n2
        else:
            return "Division by zero is not allowed."
        
    def multiply(self):
            return self.n1 * self.n2
        
        
math_obj = Math(10, 5)
math_obj.add()
math_obj.divide()
math_obj.multiply()





                    