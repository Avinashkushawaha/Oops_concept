from time import time
def get_execution_time(func_name):
    def wrapper(*args, **kwargs):
        print("Inside a decorator")
        start = time
        result = func_name(*args, **kwargs)
        end = time ()
        execution_time = end-start
        print(execution_time)
        return result
    return wrapper