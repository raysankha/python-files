##def decorator(func):
##    def wrapper():
##        print("good morning")
##        func()
##    return wrapper
##@decorator
##def result():
##    print("hello python")
##result()






##def decorator(func):
##    def wrapper():
##        print("start")
##        func()
##    return wrapper
##@decorator
##def result():
##    print("end")
##result()







##def decorator(func):
##    def wrapper():
##        print("welcome")
##        func()
##    return wrapper
##
##@decorator
##def result():
##    pass
##
##result()






##def decorator(func):
##    def wrapper(*args):
##        print("adding numbers")
##        func(*args)
##    return(wrapper)
##@decorator
##def result(a,b):
##    print(a+b)
##result(6,8)







##def decorator(func):
##    def wrapper(*args):
##        print("calculating")
##        func(*args)
##    return wrapper
##@decorator
##def square(n):
##    print(n*n)
##square(7)
        
    






##def decorator(func):
##    def wrapper():
##        print("function started")
##        func()
##        print("function finished")
##    return wrapper
##@decorator
##def result():
##    print("python")
##result()






##def decorator(func):
##    def wrapper(*args):
##        print(args)
##        func(*args)
##    return wrapper
##@decorator
##def add(a,b):
##    print(a+b)
##add(10,20)






##def my_decorator(func):
##    def wrapper(*args):
##        print("Calculating...")
##        result = func(*args)
##        return result
##    return wrapper
##
##
##@my_decorator
##def square(n):
##    return n * n
##
##
##print(square(5))







##def decorator(func):
##    def wrapper(**kwargs):
##        print("calculating...")
##        func(**kwargs)
##    return wrapper
##@decorator
##def dict(age=20,name="sankha"):
##    print(age)
##    print(name)
##dict()





##def decorator(func):
##    def wrapper(*args):
##        print("welcome")
##        result=func(*args)
##        return result
##    return wrapper
##@decorator
##def hello(a,b):
##    return a*b
##print(hello(6,8))
    
    





##def decorator(message):
##    def real_decorator(func):
##        def wrapper(*args,**kwargs):
##            print(message)
##            return func(*args,**kwargs)
##        return wrapper
##    return real_decorator
##@decorator("good morning")
##def hello():
##    print("hello world")
##
##hello()







##def dog(animal):
##    def cat(func):
##        def wrapper(*args,**kwargs):
##            print(animal)
##            func(*args,**kwargs)
##        return wrapper
##    return cat
##@dog("i am barking")
##def hello():
##    print("my name is tom")
##hello()






##def x(n):
##    def y(func):
##        def wrapper(*args,**kwargs):
##            print(n)
##            func(*args,**kwargs)
##        return wrapper
##    return y
##@x(7)
##def hello():
##    print("my name is sankha")
##
##hello()






##def decorator(n):
##    def real_decorator(func):
##        def wrapper():
##            for i in range(n):
##                func()
##        return wrapper
##    return real_decorator
##
##
##@decorator(3)
##def hello():
##    print("Hello Python")
##
##
##hello()





##def decorator(message):
##    def real_decorator(func):
##        def wrapper():
##            print(message)
##            func()
##        return wrapper
##    return real_decorator
##
##
##@decorator("Welcome Student")
##def hello():
##    print("Python is easy")
##
##
##hello()





##def outer(message):
##    def inner(func):
##        def wrapper():
##            print(message)
##            func()
##        return wrapper
##    return inner
##@outer("welcome")
##def hello():
##    print("hello python")
##hello()







##def outer(message):
##    def inner(func):
##        def wrapper():
##            print(message)
##            func()
##        return wrapper
##    return inner
##@outer("good morning")
##def hello():
##    pass
##hello()






##def outer(message):
##    def inner(func):
##        def wrapper(*args,**kwargs):
##            print(message)
##            func(*args,**kwargs)
##        return wrapper
##    return inner
##@outer("welcome")
##def hello(name="sankha",age=20):
##    print(name)
##    print(age)
##hello()
    
            




##def inner(func):
##    def wrapper():
##        result=func()
##        return result
##    return wrapper
##@inner
##def hello():
##    return "welcome"
##print(hello())





##from functools import wraps
##def decorator(func):
##    @wraps(func)
##    def wrapper(*args,**kwargs):
##        return func(*args,**kwargs)
##    return wrapper
##
##@decorator
##def hello():
##    print("hello python")
##hello()
##print(hello.__name__)






##from functools import wraps
##def decorator(func):
##    @wraps(func)
##    def wrapper():
##        func()
##    return wrapper
##@decorator
##def student():
##    print("python")
##student()
##print(student.__name__)








##from functools import wraps
##def decorator(func):
##    @wraps(func)
##    def wrapper():
##        func()
##    return wrapper
##@decorator
##def college():
##    print("studies python")
##college()
##print(college.__name__)
    





##from functools import wraps
##def decorator(func):
##    @wraps(func)
##    def wrapper():
##        print("studying")
##        func()
##    return wrapper
##@decorator
##def hello():
##    print("hello world")
##hello()
##print(hello.__name__)







##def deco1(func):
##    def wrapper():
##        print("studying")
##        func()
##    return wrapper
##def deco2(func):
##    def wrapper():
##        print("welcome")
##        func()
##    return wrapper
##
##@deco1
##@deco2
##def hello():
##    print("hello world")
##hello()









##def decorator(func):
##    def wrapper():
##        print("hello")
##        func()
##        print("hello akash")
##    return wrapper
##def order(func):
##    def wrapper():
##        print("hello python")
##        func()
##    return wrapper
##@decorator
##@order
##def result():
##    print("hello world")
##result()







##def inner(func):
##    def wrapper(*args,**kwargs):
##        print("welcome")
##        func(*args,**kwargs)
##    return wrapper
##@inner
##def student(name):
##    print(name)
##student("sankha")







##def inner(func):
##    def wrapper(*args,**kwargs):
##        print("calculating")
##        result=func(*args,**kwargs)
##        return result
##    return wrapper
##@inner
##def hello(a,b):
##    return a*b
##print(hello(8,7))
    






##from functools import wraps
##
##def decorator(func):
##    @wraps(func)
##    def wrapper():
##        func()
##    return wrapper
##
##@decorator
##def marks():
##    print("90")
##
##marks()
##print(marks.__name__)









##def inner(func):
##    def wrapper():
##        for i in range(1,4):
##            print("*")
##        func()
##    return wrapper
##@inner
##def hello():
##    pass
##hello()
    
        






##def inner(func):
##    def wrapper():
##        print("---------------")
##        func()
##    return wrapper
##@inner
##def hello():
##    print("---------------")
##hello()







##def dec(func):
##    def wrapper(*args,**kwargs):
##        print("adding numbers")
##        func(*args,**kwargs)
##    return wrapper
##@dec
##def add(a,b):
##    print(a+b)
##add(10,20)






##def dec(func):
##    def wrapper(*args,**kwargs):
##        print("returning the result of the square....")
##        result=func(*args,**kwargs)
##        return result
##    return wrapper
##@dec
##def square(n):
##    return n*n
##print(square(5))







##def dec(func):
##    def wrapper(*args,**kwargs):
##        print("puuting the value....")
##        result=func(*args,**kwargs)
##        return result
##    return wrapper
##@dec
##def student(name,age):
##    return name,age
##print(student("sankha",age=20))








##def dec(func):
##    def wrapper(*args,**kwargs):
##        print("puuting the value....")
##        result=func(*args,**kwargs)
##        return result
##    return wrapper
##@dec
##def multiply(a,b):
##    return 2*a*b
##print(multiply(3,4))







##def dec(func):
##    def wrapper():
##        pass
##        result=func()
##        print(result)
##        return result
##    return wrapper
##@dec
##def student():
##    return "i am studying python"
##print(student())







##def decorator(message):
##    def inner(func):
##        def wrapper():
##            print(message)
##            func()
##        return wrapper
##    return inner
##@decorator("good morning")
##def hello():
##    pass
##hello()







##def decorator(repeat):
##    def inner(func):
##        def wrapper():
##            print(repeat)
##            func()
##        return wrapper
##    return inner
##@decorator(3)
##def hello():
##    for i in range(1,4):
##        print(i)
##hello()








##def decorator(multiply_by):
##    def inner(func):
##        def wrapper(*args, **kwargs):
##            result = func(*args, **kwargs)
##            return result
##        return wrapper
##    return inner
##
##@decorator(3)
##def hello(a):
##    return a*3
##
##print(hello(7))
    







##def inner(func):
##    def outer():
##        print("python")
##        func()
##    return outer
##def decorator(func):
##    def wrapper():
##        print("coding")
##        func()
##    return wrapper
##@inner
##@decorator
##def hello():
##    pass
##hello()







##def inner(func):
##    def outer(*args,**kwargs):
##        result=func(*args,**kwargs)
##        if result>0:
##            print("positive")
##        else:
##            print("not positive")
##    return outer
##@inner
##def hello(a,b):
##    return a+b
##hello(7,8)
               







##from functools import wraps
##def inner(func):
##    @wraps(func)
##    def outer():
##        print("hello python")
##        func()
##    return outer
##@inner
##def hello():
##    pass
##hello()
##print(hello.__name__)







##from functools import wraps
##def outer(func):
##    @wraps(func)
##    def inner():
##        print("function is running")
##        func()
##    return inner
##@outer
##def hello():
##    pass
##hello()
        






##from functools import wraps
##def outer(func):
##    @wraps(func)
##    def inner():
##        print("sankha is playing")
##        print("rahul is sleeping")
##        func()
##    return inner
##@outer
##def hello():
##    print("hello python")
##hello()
##print(hello. __name__)






































































































































