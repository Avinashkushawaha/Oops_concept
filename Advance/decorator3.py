def error_handler(func_name):
    def wrapper(*args, **kwargs):
        print(" inside a decorator ")
        try:
         result = func_name(*args, **kwargs)
         
