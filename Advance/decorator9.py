def requires_auth(func):
    def wrapper(user):
        if not user.get("authenticated"):
            print("Access denied!")
            return
        return func(user)
    return wrapper