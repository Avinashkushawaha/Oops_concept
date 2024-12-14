def requires_auth(func):
    def wrapper(user):
        if not user.get("authenticated"):
            print("Access denied!")
            return
        return func(user)
    return wrapper

@requires_auth
def welcome(user):
    print(f"Welcome {user['name']}!")

user = {"name": "John", "authenticated": False}
welcome(user)