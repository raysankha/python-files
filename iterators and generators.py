######iterators#####-----

##numbers=[10,20,30]
##it=iter(numbers)
##print(next(it))
##print(next(it))
##print(next(it))




##name="python"
##it=iter(name)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))




##a=[2,4,6,8,10]
##it=iter(a)
##for i in it:
##    print(i)




##a=[1,2,3]
##it=iter(a)
##try:
##    while True:
##        print(next(it))
##except StopIteration:
##    print("iterator finished")
    



##x={"a":10,
##   "b":20,
##   "c":30
##   }
##it=iter(x)
##print(next(it))
##print(next(it))
##print(next(it))





##a=[10,20]
##it=iter(a)
##print(next(it, "program finished"))
##print(next(it, "program finished"))
##print(next(it, "program finished"))



##a=[7,8]
##it=iter(a)
##print(next(it))
##print(list(it))




##a=[1,2,3,4,5]
##it=iter(a)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))




##a=[10,20,30]
##it=iter(a)
##while True:
##    try:
##        print(next(it))
##    except StopIteration:
##        break





##a=[10,20,30,40,50]
##it=iter(a)
##print(next(it))
##print(next(it))
##for i in it:
##    print(i)




##a="programming"
##it=iter(a)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))




##a=[5,10,15,20,25]
##it=iter(a)
##while True:
##    try:
##        print(next(it))
##    except StopIteration:
##        break




##a=[12,25,30,45,60,75]
##it=iter(a)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##
##while True:
##    try:
##        print(next(it))
##    except StopIteration:
##        break







##a=[7,9,65,70]
##it=iter(a)
##while True:
##    try:
##        i=next(it)
##        if i>30:
##            print(i)
##    except StopIteration:
##        
##        break





##a=[1,2,3,4,5,6]
##it=iter(a)
##
##for i in it:
##
##    if i==1:
##        continue
##    print(i)





##a=[10,20,30]
##b=[100,200,300]
##it1=iter(a)
##it2=iter(b)
##while True:
##    try:
##        i=next(it1)+next(it2)
##        print(i)
##    except StopIteration:
##        break

    


##a=[6,7,8,9]
##it=iter(a)
##while True:
##    try:
##        i=next(it)
##        print(i)
##    except StopIteration:
##        break



##numbers=[10,20,30]
##it=iter(numbers)
##for i in it:
##    print(i)
##for i in it:
##    print(i)




##a="programming"
##it=iter(a)
##count=0
##for i in it:
##    if i=="m":
##        count+=1
##print(count)
    




##a=[10,20,30]
##it=iter(a)
##try:
##    while True:
##        print(next(it))
##except StopIteration:
##    print("finished")
    



##a=[10,20,30,40]
##b=[1,2,3,4]
##it1=iter(a)
##it2=iter(b)
##try:
##    while True:
##        x=next(it1)+next(it2)
##        print(x)
##except StopIteration:
##    pass




##a=[1,2,3,4,5,6]
##b=iter(a)
##c=b
##print(next(b))
##print(next(b))
##print(next(c))
##print(next(c))






##class n:
##    def __iter__(self):
##        self.x=2
##        return self
##    def __next__(self):
##        value=self.x
##        self.x+=2
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))
##print(next(it))





##class n:
##    def __iter__(self):
##        self.x=5
##        return self
##    def __next__(self):
##        value=self.x
##        self.x+=5
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))






##class n:
##    def __iter__(self):
##        self.x=10
##        return self
##    def __next__(self):
##        value=self.x
##        self.x+=10
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
        
    




##class n:
##    def __iter__(self):
##        self.x=90
##        return self
##    def __next__(self):
##        value=self.x
##        self.x+=5
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))





##class n:
##    def __iter__(self):
##        self.x=1
##        return self
##    def __next__(self):
##        value=self.x
##        self.x+=2
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
##print(next(it))
    




##class n:
##    def __iter__(self):
##        self.x=1
##        return self
##    def __next__(self):
##        value=self.x
##        self.x*=5
##        return value
##obj=n()
##it=iter(obj)
##print(next(it))
##print(next(it))
##print(next(it))

        
        


##class n:
##    def __iter__(self):
##        self.x=1
##        return self
##    def __next__(self):
##        value=self.x
##        if self.x<6:
##            self.x+=1
##            return value
##        else:
##            raise StopIteration
##a=n()
##it=iter(a)
##for i in it:
##    print(i)






##class EvenNumbers:
##    def __iter__(self):
##        self.x=2
##        return self
##    def __next__(self):
##        value=self.x
##        if self.x<11:
##            self.x+=2
##            return value
##        else:
##            raise StopIteration
##a=EvenNumbers()
##it=iter(a)
##for i in it:
##    print(i)
        




##class my_iterator:
##    def __iter__(self):
##        self.x=1
##        self.sum=0
##        return self
##    def __next__(self):
##        if self.x<5:
##            self.sum+=self.x
##            self.x+=1
##            return self.sum
##        else:
##            raise StopIteration
##a=my_iterator()
##it=iter(a)
##for i in it:
##    pass
##print(a.sum)
##           







##class my_iterator:
##    def __iter__(self):
##        self.n=n
##        self.x=1
##        self.sum=0
##        return self
##    def __next__(self):
##        if self.x<=self.n:
##            self.sum+=self.x
##            self.x+=1
##            return self.sum
##        else:
##            raise StopIteration
##n=int(input("n is:"))
##a=my_iterator()
##it=iter(a)
##for i in it:
##    pass
##print(a.sum)
           




##class n:
##    def __iter__(self):
##        self.x=10
##        return self
##    def __next__(self):
##        value=self.x
##        if self.x>=1:
##            self.x-=1
##            return value
##        else:
##            raise StopIteration
##a=n()
##it=iter(a)
##for i in it:
##    print(i)
##            
    




##class n:
##    def __iter__(self):
##        self.x=1
##        return self
##    def __next__(self):
##        
##        if self.x<=5:
##            value=self.x*self.x
##            self.x+=1
##            return value
##        else:
##            raise StopIteration
##a=n()
##it=iter(a)
##for i in it:
##    print(i)









##class n:
##    def __iter__(self):
##        self.x=1
##        return self
##    def __next__(self):
##        value=self.x
##        if self.x<=10:
##            self.x+=2
##            return value
##        else:
##            raise StopIteration
##
##
##a=n()
##it=iter(a)
##for i in it:
##    print(i)








##class z:
##    def __iter__(self):
##        self.x=1
##        self.n=n
##        return self
##    def __next__(self):
##        
##        if self.x<=10:
##            value=self.x*self.n
##            self.x+=1
##            return value
##        else:
##            raise StopIteration
##
##n=int(input("n is:"))
##a=z()
##it=iter(a)
##for i in it:
##    print(i)









##class n:
##    def __iter__(self):
##        self.x=1
##        self.fact=1
##        return self
##    def __next__(self):
##        if self.x<=5:
##            self.fact=self.fact*self.x
##            self.x+=1
##            return self.fact
##            
##        else:
##            raise StopIteration
##a=n()
##it=iter(a)
##for i in it:
##    pass
##print(a.fact)














#####generators####-----


##def numbers():
##    yield 1
##    yield 2
##    yield 3
##for i in numbers():
##    print(i)




##def demo():
##    print("start")
##    yield 10
##    print("middle")
##    yield 20
##    print("end")
##    yield 30
##x=demo()
##print(next(x))
##print(next(x))
##print(next(x))





##def numbers():
##    yield 1
##    yield 2
##x=numbers()
##print(next(x))
##print(next(x))
##try:
##    print(next(x))
##except StopIteration:
##    print("values finished")





##def numbers():
##    for i in range(1,6):
##        yield i
##for x in numbers():
##    print(x)






##def squares():
##    for i in range(1,6):
##        yield i*i
##for x in squares():
##    print(x)






##def num():
##    yield 10
##    yield 20
##    yield 30
##x=num()
##for i in num():
##    print(i)
##
##print("second time:")
##for i in num():
##    print(i)




##squares=(x*x for x in range(1,6))
##for i in squares:
##    print(i)





##def orders():
##    yield "order 100"
##    yield "order 101"
##    yield "order 102"
##for i in orders():
##    print("processing:",i)





##def count():
##    for i in range(1,11):
##        yield i
##for i in count():
##    print(i)




##def even():
##    for i in range(2,11,2):
##        yield i
##for i in even():
##    print(i)




##def cube():
##    for i in range(1,6):
##        yield i*i*i
##for i in cube():
##    print(i)





##def num():
##    yield 10
##    yield 20
##    yield 30
##x=num()
##print(next(x))
##print(next(x))
##print(next(x))





##def table():
##    n=int(input("n is:"))
##    for i in range(1,11):
##        yield n*i
##for i in table():
##    print(i)





##def num():
##    for i in range(1,21):        
##        if i%3==0 and i%5!=0:
##             yield i
##for i in num():
##    print(i)





##def num():
##    yield 20
##    yield 30
##    yield 40
##g=num()
##print(next(g,"finished"))
##print(next(g,"finished"))
##print(next(g,"finished"))
##print(next(g,"finished"))




##numbers=[-5,10,-3,20,7,-1,30]
##def num():
##    for i in numbers:
##        if i>0:
##            yield i
##for i in num():
##    print(i)
##            
    


##numbers = [2, 4, 6, 8, 10]
##def num():
##    for i in numbers:
##        yield i*2
##for i in num():
##    print(i)




##n=int(input("n is:"))
##def num():
##    for i in range(1,n+1):
##        yield i
##for i in num():
##    print(i)



##def num():
##    total=0
##    for i in range(1,6):
##        total+=i
##    yield total
##for i in num():
##    print(i)




##name="python"
##def num():
##    for i in str(name):
##        yield i
##for i in num():
##    print(i)



##numbers = [1, 2, 3, 4, 5, 6, 7, 8]
##def num():
##    for i in numbers:
##        if i%2==0:
##            yield i*i
##for i in num():
##             print(i)





##def num():
##    for i in range(1,101):
##        yield i
##g=num()
##print(next(g))
##print(next(g))
##print(next(g))
##print(next(g))
##print(next(g))



##n = 12345
##def num():
##    reverse=""
##    for i in str(n):
##        reverse=i+reverse
##    yield reverse
##for i in num():
##    print(i)
        




##n=12345
##def num():
##    sum=0
##    for i in str(n):
##        sum+=int(i)
##    yield sum
##for i in num():
##    print(i)





##numbers = [-6, 9, 12, 4, 15, 20, 30, -3]
##def num():
##    for i in numbers:
##        if i>0 and i>5 and i%3==0:
##            yield i
##for i in num():
##    print(i)





##numbers = [2, 5, 7, 10, 12]
##def num():
##    for i in numbers:
##        yield i*i
##for i in num():
##    print(i)





##numbers = [10, 20, 5, 15, 10]
##def num():
##    sum=0
##    for i in numbers:
##        sum+=i
##    yield sum
##for i in num():
##    print(i)
        





##def my_gen():
##    x=yield 10
##    yield x
##g=my_gen()
##print(next(g))
##print(g.send(65))





##def my_gen():
##    yield 10
##    yield 20
##    yield 30
##g=my_gen()
##print(next(g))
##g.close()
##print(next(g))




##def gen():
##    x=yield 10
##    y=yield x+5
##    yield y+2
##g=gen()
##print(next(g))
##print(g.send(20))
##print(g.send(30))





##def n():
##    x=yield 10
##    yield x
##g=n()
##print(next(g))
##print(g.send(70))






##def number():
##    yield 1
##    yield 2
##    yield 3
##g=number()
##print(next(g))
##print(next(g))
##g.close()
##print(next(g))





##def num():
##    x=yield 100
##    y=yield x
##    yield y
##g=num()
##print(next(g))
##print(g.send(20))
##print(g.send(30))





##def num():
##    yield 10
##    yield 20
##    yield 30
##
##g = num()
##print(next(g))
##g.close()
##print(next(g))




##def num():
##    x=yield 2
##    yield x*x
##g=num()
##print(next(g))
##print(g.send(5))





##def numbers():
##    yield 1
##    yield 2
##    yield 3
##    yield 4
##
##g = numbers()
##print(next(g))
##print(next(g))
##g.close()




##def n():
##    x=yield 10
##    yield x
##g=n()
##print(next(g))
##print(g.send(50))
##g.close()




##def test():
##    x = yield 10
##    yield x
##
##g = test()
##print(next(g))
##print(g.send(5))




##def test():
##    x=yield 90
##    y=yield 80
##    z=yield y
##g=test()
##print(next(g))
##print(next(g))
##print(g.send(50))






##def test():
##    try:
##        yield 1
##        yield 2
##    finally:
##        print("Generator closed")
##g = test()
##print(next(g))
##g.close()





##numbers=[[1,2],[3,4,5],[6,7]]
##def n():
##    for i in numbers:
##        for j in i:
##            yield j
##for x in n():
##    print(x)





##def inner():
##    yield 10
##    yield 20
##def outer():
##    yield inner()
##g=outer()
##g2=next(g)
##for i in g2:
##    print(i)





##def inner():
##    yield 10
##    yield 20
##    yield 30
##
##def outer():
##    yield from inner()
##
##for i in outer():
##    print(i)





##def inner():
##    yield 1
##    yield 2
##
##def outer():
##    yield from inner()
##    yield 3
##
##for i in outer():
##    print(i)





##def even():
##    yield 2
##    yield 4
##    yield 6
##def all_numbers():
##    yield from even()
##for i in all_numbers():
##    print(i)
    



##def first():
##    yield 1
##    yield 2
##def second():
##    yield 3
##    yield 4
##def third():
##    yield from first()
##    yield from second()
##for i in third():
##    print(i)




##
##def first():
##    yield "python"
##    yield "java"
##def second():
##    yield from first()
##    yield "c++"
##for i in second():
##    print(i)





##def first():
##    yield 1
##    yield 2
##    yield 3
##def second():
##    yield 4
##    yield 5
##def third():
##    yield 6
##    yield 7
##    yield 8
##def fourth():
##    yield from first()
##    yield from second()
##    yield from third()
##for i in fourth():
##    print(i)




##def squares():
##    yield 1
##    yield 4
##    yield 9
##def outer():
##    yield from squares()
##    yield 16
##for i in outer():
##    print(i)


























































