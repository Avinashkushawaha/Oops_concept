def gen(n):
    for i in range(n):
        yield i

ob1 = gen(1000 )
print(next(ob1)) 
print(next(ob1))   
print(next(ob1))  
print(next(ob1)) 
print(next(ob1))
print(next(ob1))    