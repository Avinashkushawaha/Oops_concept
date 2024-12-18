from time import ctime
def delay_invoked_time(func):
    def wrapper(*args, **kwargs):
        print(f"{func name} invoked at {ctime()}")
