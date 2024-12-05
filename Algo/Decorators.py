def mydecorator(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        function(*args, **kwargs)

    return wrapper
@mydecorator
def hello(person):
    print("Hello {person}!")

hello("mike")   
