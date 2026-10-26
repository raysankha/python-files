##def add(*args):
##    print(args)
##add(10,20,30,40)




##def add(*args):
##    total=0
##    for i in args:
##        total+=i
##    print(total)
##add(10,20,30)




##def student(**kwargs):
##    print(kwargs)
##student(name="rahul",age=20,city="kolkata")




##def student(**kwargs):
##    for key,value in kwargs.items():
##        print(key,value)
##student(name="rahul",age=20,course="cse")




##def demo(*args,**kwargs):
##    print(args)
##    print(kwargs)
##demo(10,20,name="rahul",age=20)





##def show(**kwargs):
##    print(kwargs['name'])
##show(name="amit",age=21)





##def display(*args,**kwargs):
##    for key,value in kwargs.items():
##        print(key,value)
##    print(args)
##display(10,20,30,name="rahul",age=30)





##def find_max(*args):
##    max=args[0]
##    for i in args:
##        if i>max:
##            max=i
##    print(max)
##find_max(12,45,7,89,23)
##find_max(100,50,75)







##def find_min(*args):
##    min=args[0]
##    for i in args:
##        if i<min:
##            min=i
##    print(min)
##find_min(12,45,7,89,23)
##find_min(100,50,75)






##def find_student(**kwargs):
##    for i in kwargs:
##        if kwargs[i]>40:
##            print(i)
##find_student(rahul=75,amit=32,priya=90,rohit=25)





##def calculate(*args,**kwargs):
##    total=0
##    for i in args:
##        total+=i
##    print("total:",total)
##    for key,value in kwargs.items():
##        print(key,value)
##        
##calculate(10,20,30,name="rahul",age=20)

        




##def student(name,*args):
##    print(name)
##    print(args)
##student("rahul",80,75,90)





##def add(a,*args):
##    print(a)
##    print(args)
##add(6,79,90,81)




 

##def add(a,b,c):
##    print(a+b+c)
##numbers=[10,20,30]
##add(*numbers)






##def student(name,age):
##    print(name,age)
##data={"name":"sankha","age":20}
##student(**data)






##def add(*args):
##    print(sum(args))
##add(2,3,4)






##def even(*args):
##    for i in args:
##        if i%2==0:
##            print(i)
##even(10,21,35,41)






##def total(*args):
##    count=0
##    for i in args:
##        count+=1
##    print(count)
##total(10,20,30,40,90)
##    






##def pos(*args):
##    total=0
##    for i in args:
##        if i>0:
##            total+=i
##    print(total)
##pos(10,-20,30,-40,-80,50)







##def num(*args):
##    for i in reversed(args):
##        print(i)
##num(10,20,30)





##def num(*args):
##    total=0
##    for i in args:
##        total+=i
##    average=total/3
##    print(average)
##num(10,20,30)





##def student(**kwargs):
##    print(kwargs)
##student(name="sankha",age=21,city="bankura")





##def student(**kwargs):
##    for key,value in kwargs.items():
##        print(key,value)
##student(name="sankha",age=21,city="bankura")




##def student(**kwargs):
##    sum=0
##    for i in kwargs.values():
##        sum+=i
##    print(sum)
##student(sankha=80, rahul=90, akash=70)





##def person(**kwargs):
##    if "age" in kwargs:
##        print("key present")
##    else:
##        print("not present")
##
##person(name="sankha",age=21)







##def student(*args,**kwargs):
##    print(args)
##    print(kwargs)
##student("sankha",75,city="bankura",age=25)






##def student(*args,**kwargs):
##    max=0
##    for i in args:
##        if i>max:
##            max=i
##    print(max)
##    print(kwargs)
##student(25,30,40,name="sankha",age=22)







##def num(a,b,c):
##    print(a,b,c)
##x=[10,20,30]
##num(*x)




##def dict(name,age):
##    print(name,age)
##x={"name":"sankha","age":20}
##dict(**x)




##def num(a,b):
##    print(a+b)
##x=[50,60]
##num(*x)





##def dict(name,age,city):
##    print(name,age,city)
##x={"name":"sankha","age":21,"city":"bankura"}
##dict(**x)






##def dict(a,b,course,college):
##    print(a,b,course,college)
##x=20,30
##y={"course":"cse","college":"sanaka"}
##dict(*x,**y)






##def player(name,*recent_scores):
##    print("name:",name)
##    print("recent_scores:",recent_scores)
##player("devillers",17,127,85)





##def player(name,*recent_scores,**details):
##    print("name:",name)
##    print("recent_scores:",recent_scores)
##    print("details:",details)
##player("devillers",90,83,105,country="south africa",team="rcb")






##def player(name,*scores,**details):
##    print(name)
##    print(scores)
##    print(details)
##player("kohli",133,29,0,country="india")
##player("rohit",237,85,40,city="mumbai")
    




##def num(name,*a):
##    print("name:",name)
##    print("a:",a)
##num("sankha",70,80,90)






##def student(name):
##    print(name)
##student("sankha")





##def student(name="Sankha"):
##    print(name)
##
##student()





##def student(name="sankha",age=20,city="bankura"):
##    print(name)
##    print(age)
##    print(city)
##student()





##def student(name,city="bankura"):
##    print(name)
##    print(city)
##student("sankha")
##student("rahul","kolkata")





##def student(name="sankha",city="bankura"):
##    print(name,city)
##student(city="kolkata")





##def student(name="sankha",*marks):
##    print(name)
##    print(marks)
##
##student("rahul",80,90,100)





##def x(name="sankha"):
##    print(name)
##x()





##def x(name,age=20):
##    print(name)
##    print(age)
##x("sankha")





##def x(city="bankura"):
##    print(city)
##x()
##x(city="kolkata")





##def x(a=10,b=20):
##    print(a+b)
##x()





##def x(name="sankha",age=20,city="bankura"):
##    print(name,age,city)
##x()
##x(age=21)





##def x(name="sankha",*marks,**details):
##    print(name)
##    print(marks)
##    print(details)
##x("sankha",75,80,90,city="bankura",age=21)





##def x(name="sankha",age=20):
##    print(name,age)
##x()





##def x(name="sankha",*marks):
##    total=0
##    for i in marks:
##        total+=i
##    print(total)
##    print(name)
##    print(marks)
##x("akash",75,80,90)
##    





##def x(name="sankha",**details):
##    print(name)
##    print(details)
##x("sankha",city="bankura",age=21)






##def student(name, *, age):
##    print(name, age)
##
##student("Sankha", age=20)




##def student(name, *, age):
##    print(name, age)
##
##student("Sankha", age=20)






##def show(a,b,*,c,d):
##    print(a,b,c,d)
##show(10,20,c=30,d=40)





##def student(name,*,age=20,city="bankura"):
##    print(name,age,city)
##student("sankha")
##student("rahul",age=21)
##student("akash",city="kolkata")





##def student(name,*marks,city):
##    print(name)
##    print(marks)
##    print(city)
##student("sankha",70,80,90,city="bankura")




##def student(name,**details):
##    print(name)
##    print(details)
##student("sankha",age=20,city="bankura")






##def student(name,*,age):
##    print(name)
##    print(age)
##student("sankha",age=21)





##def student(a,*,b=10):
##    print(a+b)
##student(6,b=10)




##def student(name,*marks,city):
##    print(name)
##    print(marks)
##    print(city)
##student("sankha",76,80,90,city="bankura")





##def calculation(a,b,*,operation="add"):
##    if operation=="add":
##        print(a+b)
##    else:
##        print(a*b)
##calculate(10,20)
##calculation(10,20,operation="multiply")
    




##def area(length,width,*,unit="cm"):
##    print(length*width)
##    print(unit)
##area(8,7,unit="10cm")






##def employee(name,*skills,city):
##    print(name)
##    print(skills)
##    print(city)
##employee("sankha","btech cse",city="agra")







##def show(a,b,/,c,d):
##    print(a,b,c,d)
##show(10,20,c=19,d=88)





##def student(name="Sankha", age=20, /):
##    print(name, age)
##
##student()
##student("Rahul", 21)







##def student(name,/):
##    print(name)
##student("sankha")





##def student(a,b,/):
##    print(a+b)
##student(10,12)




##def student(a,/,b):
##    print(a,b)
##student(10,b=7)





##def student(name,age=20,/):
##    print(name,age)
##student("sankha",20)










































































