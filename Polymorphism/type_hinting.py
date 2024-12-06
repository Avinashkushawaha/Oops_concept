def myfunction(myparameter: int) -> str:
    return f"{myparameter + 10}"

def otherfunction(otherparameter: str):
    print(otherparameter)

otherfunction(myfunction(20))

def dosth(param: list[int]):
