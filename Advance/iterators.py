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

num = "classroom"
iter1 = iter(num)
# for i in num:
print(next(iter1))
print(next(iter1))
