from time import ctime
def delay_invoked_time(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} invoked at {ctime()}")
        return func(*args, **kwargs)
    return wrapper

def Math_deco(cls):
    for name, method in cls.__dict__.items():
        if callable(method):

            decorated_method = delay_invoked_time(method)
            setattr(cls, name, decorated_method)
    return cls

@Math_deco
class WhatsDown:
    def change_dp(self):
        print('changing dp') 

    def upload_state(self):
        print("uploading status")

    def react (self):
        print('reacting to msg')

whats_app = WhatsDown()
whats_app.change_dp()
whats_app.upload_state()
whats_app.react()                        

