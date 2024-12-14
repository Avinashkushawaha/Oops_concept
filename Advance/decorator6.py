def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function
def display():
    print("Display function ran")

decorated_display = decorator_function(display)
decorated_display()