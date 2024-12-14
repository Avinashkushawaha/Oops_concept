def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log_decorator
def add(a, b):
    return a + b

print(add(2, 3))