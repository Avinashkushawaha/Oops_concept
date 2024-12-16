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
        if callable(getattr(cls_name, attr)) and not attr.swithswith("__"):
            method = getattr(cls_name, attr)
            decorated_method = method_decoration(method)
            
                    