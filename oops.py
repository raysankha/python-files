##class Student:
##
##    def __init__(self, name, marks):
##        self.name = name
##        self.marks = marks
##        print("adding new student in database..")
##
##
##s1 = Student("sankha", 95)
##print(s1.name, s1.marks)
##
##s2 = Student("arjun", 93)
##print(s2.name, s2.marks)



##class car:
##    def __init__(self,color,brand):
##        self.color=color
##        self.brand=brand
##        print("adding car structure in garage...")
##car1=car("blue","thar")
##print(car1.color,car1.brand)
##
##car2=car("red","maruti suzuki")
##print(car2.color,car2.brand)




##class student:
##    college_name="sanaka"
##    def __init__(self,name,address,district):
##        self.name=name
##        self.address=address
##        self.district=district
##s1=student("sankha","indpur","bankura")
##print(s1.name,s1.address,s1.district)
##print(student.college_name)




##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def welcome(self):
##        print("hello world")
##s1=student("sankha",97)
##print(s1.name,s1.marks)
##s1.welcome()









##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def welcome(self):
##        print("hello world")
##    def get_marks(self):
##        return self.marks
##s1=student("sankha",97)
##print(s1.name,s1.marks)
##s1.welcome()
##print(s1.get_marks())









##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def average(self):
##        sum=80+96+67
##        print(sum/3)
##s1=student("sankha",[80,96,67])
##print(s1.name,s1.marks)
##s1.average()
  
    



##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def average(self):
##        sum=80+96+67
##        print(sum/3)
##    @staticmethod
##    def school():
##        print("indpur goenka")
##s1=student("sankha",[80,96,67])
##print(s1.name,s1.marks)
##s1.average()
##s1.school()








##class car:
##    def __init__(self,brand):
##        self.brand=brand
##    def display(self):
##        print(self.brand)
##car1=car("maruti")
##car1.display()






##class dog:
##    def __init__(self, name):
##        self.name = name
##
##    def bark(self):
##        print("dog is barking")
##
##d1 = dog("tom")
##d1.bark()




##class mobile:
##    def __init__(self,brand,price):
##        self.brand=brand
##        self.price=price
##    def display(self):
##        print(self.brand,self.price)
##m1=mobile("vivo t2x",15000)
##m1.display()







##class rectangle:
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##    def area(self):
##        print(self.length*self.width)
##r1=rectangle(10,5)
##r1.area()



##class student:
##    def __init__(self, name,marks):
##        self.name=name
##        self.marks=marks
##    def result(self):
##        
##        if(self.marks)>=40:
##           print("pass")
##        else:
##            print("fail")
##s1=student("sankha",99)
##s1.result()
##        
        





##class calculator:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def add(self):
##        print(self.a+self.b)
##    def multiply(self):
##        print(self.a*self.b)
##c1=calculator(50,70)
##c1.add()
##c1.multiply()


        
    





##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def display_marks(self):
##        for i in self.marks:
##            print(i)
##
##s1=student("sankha",[70,86,90,65,99])
##s1.display_marks()
##            
        



###encapsulation--------


##class bankaccount:
##    def __init__(self,account_no,balance):
##        self.account_no=account_no
##        self.__balance=balance
##
##    def show_balance(self):
##        print(self.__balance)
##b1=bankaccount(722136,50000)
##b1.show_balance()







##class bankaccount:
##    def __init__(self,balance):
##        self.__balance=balance
##
##    def deposit(self,amount):
##        self.__balance+=amount
##        
##
##    def withdraw(self,amount):
##        if(amount<=self.__balance):
##            
##            self.__balance-=amount
##        else:
##            print("insufficient balance")
##    def show_balance(self):
##        print(self.__balance)
##
##        
##b1=bankaccount(50000)
##b1.deposit(6000)
##b1.withdraw(5000)
##b1.show_balance()





##class employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.__salary=salary
##    def increase_salary(self,amount):
##        self.__salary+=amount
##    def show_salary(self):
##        print(self.__salary)
##e1=employee("sankha",60000)
##e1.increase_salary(5000)
##e1.show_salary()
        







##class product:
##    def __init__(self,name,price):
##        self.name=name
##        self.__price=price
##    def discount(self,amount):
##        self.__price-=amount
##    def show_price(self):
##        print(self.__price)
##p1=product("sankha",5000)
##p1.discount(800)
##p1.show_price()



####abstraction---------



##from abc import ABC,abstractmethod
##class animal(ABC):
##    @abstractmethod
##    def sound(self):
##        pass
##class dog(animal):
##    def sound(self):
##        print("bark")
##class cat(animal):
##    def sound(self):
##        print("meow")
##d1=dog()
##d1.sound()
##c1=cat()
##c1.sound()






##from abc import ABC,abstractmethod
##class shape(ABC):
##    @abstractmethod
##    def area(self):
##        pass
##class circle(shape):
##    def area(self):
##        print("circle area")
##
##c1=circle()
##c1.area()









##from abc import ABC,abstractmethod
##class vehicle(ABC):
##    @abstractmethod
##    def start(self):
##        pass
##class car(vehicle):
##    def start(self):
##        print("car started")
##c1=car()
##c1.start()







##from abc import ABC,abstractmethod
##class student(ABC):
##    @abstractmethod
##    def study(self):
##        pass
##class collegestudent(student):
##    def study(self):
##        print("student is studying")
##c1=collegestudent()
##c1.study()






##from abc import ABC,abstractmethod
##class vehicle(ABC):
##    @abstractmethod
##    def start(vehicle):
##        pass
##class car(vehicle):
##    def start(self):
##        print("car starts with key")
##class bike(vehicle):
##    def start(self):
##        print("bike starts with button")
##c1=car()
##c1.start()
##b1=bike()
##b1.start()

        



##from abc import ABC,abstractmethod
##class employee(ABC):
##    @abstractmethod
##    def calculate_salary(self):
##        pass
##class fulltimeemployee(employee):
##    def __init__(self,salary):
##        self.salary=salary
##    def calculate_salary(self):
##        print(self.salary)
##f1=fulltimeemployee(80000)
##f1.calculate_salary()
##        
        
        




##from abc import ABC,abstractmethod
##class shape(ABC):
##    @abstractmethod
##    def area(self):
##        pass
##class rectangle(shape):
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##    def area(self):
##        print(self.length*self.width)
##class circle(shape):
##    def __init__(self,radius):
##        self.radius=radius
##    def area(self):
##        print(3.14*self.radius*self.radius)
##r1=rectangle(10,5)
##r1.area()
##c1=circle(5)
##c1.area()

    





##from abc import ABC,abstractmethod
##class payment(ABC):
##    @abstractmethod
##    def pay(self):
##        pass
##class upipayment(payment):
##    def pay(self):
##        print("payment done using upi")
##class card(payment):
##    def pay(self):
##        print("payment done using card")
##
##u1=upipayment()
##u1.pay()
##c1=card()
##c1.pay()




##from abc import ABC,abstractmethod
##class payment(ABC):
##    @abstractmethod
##    def pay(self):
##        pass
##class upi(payment):
##    def __init__(self,amount):
##        self.amount=amount
##    def pay(self):
##        print(self.amount)
##class card(payment):
##    def __init__(self,amount):
##        self.amount=amount
##    def pay(self):
##        print(self.amount)
##class cash(payment):
##    def __init__(self,amount):
##        self.amount=amount
##    def pay(self):
##        print(self.amount)
##u1=upi(500)
##u1.pay()
##c1=card(1000)
##c1.pay()
##c2=cash(300)
##c2.pay()







##from abc import ABC,abstractmethod
##class result(ABC):
##    
##    @abstractmethod
##    def calculate(self):
##        pass
##    
##            
##class student(result):
##    def __init__(self,name,mark1,mark2,mark3):
##        self.name=name
##        self.mark1=mark1
##        self.mark2=mark2
##        self.mark3=mark3
##        
##    def calculate(self):
##        average=(self.mark1+self.mark2+self.mark3)/3
##        if (average>=40):
##            print("pass")
##        else:
##            print("fail")
##
##    
##s1=student("sankha",50,80,70)
##s1.calculate()
        







##from abc import ABC,abstractmethod
##class employee(ABC):
##    
##    @abstractmethod
##    def salary(self):
##        pass    
##class fulltimeemployee(employee):
##    def __init__(self,name,monthly_salary):
##        self.name=name
##        self.monthly_salary=monthly_salary
##    def salary(self):
##        print(self.monthly_salary*12)
##        
##f1=fulltimeemployee("sankha",70000)
##f1.salary()








#####inheritance------



##class animal:
##    def eat(self):
##        print("animal is eating")
##class dog(animal):
##    pass
##d1=dog()
##d1.eat()








##class person:
##    def __init__(self,name):
##        self.name=name
##    
##class student(person):
##    pass
##s1=student("sankha")
##print(s1.name)







##class vehicle:
##    def start(self):
##        print("car started")
##class car(vehicle):
##    pass
##c1=car()
##c1.start()



            
##class employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.salary=salary
##class manager(employee):
##    pass
##m1=manager("sankha",50000)
##print(m1.name)
##print(m1.salary)






##class animal:
##    def sound(self):
##        pass
##class dog(animal):
##    def sound(self):
##        print("dog barks")
##d1=dog()
##d1.sound()







##class shape:
##    def area(self):
##        pass
##class rectangle(shape):
##    def __init__(self,length,width):
##        self.length=length
##        self.width=width
##    def area(self):
##        print(self.length*self.width)
##r1=rectangle(5,7)
##r1.area()






##class bankaccount:
##    def __init__(self,balance):
##        self.balance=balance
##class savingaccount(bankaccount):
##    pass
##s1=savingaccount(5000)
##print(s1.balance)






##class School:
##    school_name = "ABC School"
##
##class Student(School):
##    pass
##
##s1 = Student()
##
##print(s1.school_name)





##class animal:
##    def __init__(self,name):
##        self.name=name
##    def eat(self):
##        print("animal is eating")
##class dog(animal):
##    def bark(self):
##        print("dog is barking")
##
##
##d1=dog("tom")
##d1.bark()
##d1.eat()







##class employee:
##    def __init__(self,name,salary,department):
##        self.name=name
##        self.salary=salary
##        self.department=department
##class manager(employee):
##    pass
##m1=manager("sankha",50000,"cse")
##print(m1.name)
##print(m1.salary)
##print(m1.department)






##class person:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##class student(person):
##    def __init__(self,name,age,marks):
##        super().__init__(name,age)
##        self.marks=marks
##    def display(self):
##        print(self.name,self.age,self.marks)
##s1=student("sankha",21,85)
##s1.display()

        






##class vehicle:
##    def __init__(self,brand,speed):
##        self.brand=brand
##        self.speed=speed
##class car(vehicle):
##    def __init__(self,brand,speed,fuel_type):
##        super().__init__(brand,speed)
##        self.fuel_type=fuel_type
##    def display(self):
##        print(self.brand,self.speed,self.fuel_type)
##c1=car("bmw",75,"petrol")
##c1.display()
##    
    
    
##
##class animal:
##    def __init__(self,name):
##        self.name=name
##    def sound(self):
##        pass
##class dog(animal):
##    def sound(self):
##        print("bark")
##d1=dog("tom")
##d1.sound()
##print(d1.name)




##class employee:
##    def __init__(self,name,salary):
##        self.name=name
##        self.salary=salary
##class manager(employee):
##    def __init__(self,name,salary,department):
##        super().__init__(name,salary)
##        self.department=department
##    def display(self):
##        print(self.name,self.salary,self.department)
##m1=manager("sankha",75000,"cse")
##m1.display()
##    
    





##class vehicle:
##    def __init__(self,brand,model):
##        self.brand=brand
##        self.model=model
##class car(vehicle):
##    def __init__(self,brand,model,price):
##        super().__init__(brand,model)
##        self.price=price
##    def display(self):
##        print(self.brand,self.model,self.price)
##c1=car("bmw",9,100000)
##c1.display()




##
##class animal:
##    def sound(self):
##        print("animal makes a sound")
##class dog(animal):
##    def sound(self):
##        super().sound()
##        print("dog barks")
##d1=dog()
##d1.sound()






##class animal:
##    def eat(self):
##        print("animal is eating")
##class dog(animal):
##    def bark(self):
##        print("dog is barking")
##class puppy(dog):
##    def play(self):
##        print("puppy is playing")
##p1=puppy()
##p1.play()
##p1.bark()
##p1.eat()







##class bankaccount:
##    def __init__(self,balance):
##        self.balance=balance
##    def deposit(self,amount):
##        self.balance+=amount
##class savingsaccount(bankaccount):
##    def __init__(self,balance,interest):
##        super().__init__(balance)
##        self.interest=interest
##s1=savingsaccount(50000,5)
##s1.deposit(5000)
##print(s1.balance)
   
        




##class employee:
##    def display(self):
##        print("employee")
##class manager(employee):
##    def display(self):
##        super().display()
##        print("manager")
##m1=manager()
##m1.display()






##class vehicle:
##    def __init__(self,brand):
##        self.brand=brand
##class car(vehicle):
##    def __init__(self,brand,model):
##        super().__init__(brand)
##        self.model=model
##class electriccar(car):
##    def __init__(self,brand,model,battery):
##        super().__init__(brand,model)
##        self.battery=battery
##e1=electriccar("bmw",7,10000)
##print(e1.brand)
##print(e1.model)
##print(e1.battery)






##polymorphism------



##class dog:
##    def sound(self):
##        print("dog barks")
##class cat:
##    def sound(self):
##        print("cat meows")
##d1=dog()
##d1.sound()
##c1=cat()
##c1.sound()






##class car:
##    def move(self):
##        print("car is moving")
##class bike:
##    def move(self):
##        print("bike is moving")
##
##b1=bike()
##b1.move()
##c1=car()
##c1.move()





##class dog:
##    def sound(self):
##        print("barks")
##class cat:
##    def sound(self):
##        print("meows")
##class cow:
##    def sound(self):
##        print("moos")
##animals=[dog(),cat(),cow()]
##for animal in animals:
##    animal.sound()






##class animal:
##    def sound(self):
##        pass
##class dog(animal):
##    def sound(self):
##        print("barks")
##class cat(animal):
##    def sound(self):
##        print("meows")
##
##
##c1=cat()
##c1.sound()
##d1=dog()
##d1.sound()






##class employee:
##    def work(self):
##        print("employee is working")
##class manager:
##    def work(self):
##        print("manager is managing the team")
##        
##    
##
##employees=[employee(),manager()]
##for employee in employees:
##    employee.work()




##class upi:
##    def pay(self):
##        print("payment through upi")
##class card:
##    def pay(self):
##        print("payment through card")
##payments=[upi(),card()]
##for payment in payments:
##    payment.pay()






##class dog:
##    def sound(self):
##        print("barks")
##class cat:
##    def sound(self):
##        print("meows")
##class cow:
##    def sound(self):
##        print("moos")
##
##animals=[dog(),cat(),cow()]
##for animal in animals:
##    animal.sound()





##class car:
##    def fare(self):
##        print(100)
##class bus:
##    def fare(self):
##        print(50)
##class train:
##    def fare(self):
##        print(80)
##transports=[car(),bus(),train()]
##for transport in transports:
##    transport.fare()



##duck typing----



##class dog:
##    def sound(self):
##        print("barks")
##class cat:
##    def sound(self):
##        print("meows")
##
##def make_sound(animal):
##    animal.sound()
##    
##d=dog()
##c=cat()
##make_sound(c)
##make_sound(d)






##class car:
##    def start(self):
##        print("car started")
##class bike:
##    def start(self):
##        print("bike started")
##def a_start(vehicle):
##    vehicle.start()
##c=car()
##b=bike()
##a_start(c)
##a_start(b)





##class dog:
##    def run(self):
##        print("dog runs")
##class bird:
##    def run(self):
##        print("bird runs")
##def make_run(animal):
##    animal.run()
##d=dog()
##b=bird()
##make_run(d)
##make_run(b)





##class upi:
##    def pay(self):
##        print("payment through upi")
##class card:
##    def pay(self):
##        print("payment through card")
##def a_pay(payment):
##    payment.pay()
##u=upi()
##c=card()
##a_pay(u)
##a_pay(c)




##class email:
##    def send(self):
##        print("email sent msg")
##class sms:
##    def send(self):
##        print("sms sent msg")
##class whatsapp:
##    def send(self):
##        print("whatsapp sent msg")
##def a_send(notification):
##    notification.send()
##e=email()
##s=sms()
##w=whatsapp()
##a_send(e)
##a_send(s)
##a_send(w)




##class add:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def calculate(self):
##        print(self.a+self.b)
##class multiply:
##    def __init__(self,a,b):
##        self.a=a
##        self.b=b
##    def calculate(self):
##        print(self.a*self.b)
##def x_calculate(math):
##    math.calculate()
##a1=add(5,6)
##m1=multiply(5,6)
##x_calculate(a1)
##x_calculate(m1)





####operator overloading---



##class number:
##    def __init__(self,value):
##        self.value=value
##    def __add__(self,other):
##        return self.value+other.value
##a=number(60)
##b=number(50)
##print(a+b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __sub__(self,other):
##        return self.value-other.value
##a=number(60)
##b=number(50)
##print(a-b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __mul__(self,other):
##        return self.value*other.value
##a=number(6)
##b=number(7)
##print(a*b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __truediv__(self,other):
##        return self.value/other.value
##        
##
##a=number(8)
##b=number(2)
##print(a/b)






##class number:
##    def __init__(self,value):
##        self.value=value
##    def __mod__(self,other):
##        return self.value%other.value
##        
##
##a=number(8)
##b=number(2)
##print(a%b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __eq__(self,other):
##        return self.value==other.value
##        
##
##a=number(8)
##b=number(8)
##print(a==b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __lt__(self,other):
##        return self.value<other.value
##        
##
##a=number(8)
##b=number(2)
##print(a<b)




##class number:
##    def __init__(self,value):
##        self.value=value
##    def __gt__(self,other):
##        return self.value>other.value
##        
##
##a=number(8)
##b=number(2)
##print(a>b)






##class student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##    def __gt__(self,other):
##        return self.marks>other.marks
##a=student("sankha",75)
##b=student("rahul",80)
##print(a>b)






##class money:
##    def __init__(self,money):
##        self.money=money
##    def __add__(self,other):
##        return self.money+other.money
##a=money(750)
##b=money(7)
##print(a+b)




##class product:
##    def __init__(self,name,money):
##        self.name=name
##        self.money=money
##    def __add__(self,other):
##        return self.money+other.money
##
##a=product("laptop",50000)
##b=product("phone",6000)
##print(a+b)





##class number:
##    def __init__(self,value):
##        self.value=value
##    def __add__(self,other):
##         return self.value+other.value
##    def __sub__(self,other):
##        return self.value-other.value
##    def __mul__(self,other):
##        return self.value*other.value
##a=number(10)
##b=number(20)
##print(a+b)
##print(a-b)
##print(a*b)

    





####################PROJECTS-------------------------------------------------


#1. student management system.


##class student:
##    def __init__(self,name,roll,marks):
##        self.name=name
##        self.roll=roll
##        self.marks=marks
##    def display_info(self):
##        print(self.name)
##        print(self.roll)
##        print(self.marks)
##    def is_pass(self):
##        if(self.marks>=40):
##            print("pass")
##        else:
##            print("not")
##s1=student("sankha",104,75)
##s1.display_info()
##s1.is_pass()










#2. bank account.


##class bankaccount:
##    def __init__(self,holder,acc_no,balance):
##        self.holder=holder
##        self.acc_no=acc_no
##        self.balance=balance
##    def deposit(self,amount):
##        self.balance+=amount
##    def withdraw(self,amount):
##        self.balance-=amount
##    def check_balance(self):
##        print(self.balance)
##
##
##b1=bankaccount("sankha",722136,5000)
##b1.deposit(5000)
##b1.withdraw(400)
##b1.check_balance()









#3.employee management.


##class employee:
##    def work(self):
##        pass
##class manager(employee):
##    def work(self):
##        print("manager works")
##class devoloper(employee):
##    def work(self):
##        print("devoloper works")
##m1=manager()
##m1.work()
##d1=devoloper()
##d1.work()





#4.create a calculator using oops.

##class number:
##    def __init__(self,value):
##        self.value=value
##    def __add__(self,other):
##        return self.value+other.value
##    def __sub__(self,other):
##        return self.value-other.value
##    def __mul__(self,other):
##        return self.value*other.value
##    def __truediv__(self,other):
##        return self.value/other.value
##    def __mod__(self,other):
##        return self.value%other.value
##    def __eq__(self,other):
##        return self.value==other.value
##    def __lt__(self,other):
##        return self.value<other.value
##    def __gt__(self,other):
##        return self.value>other.value
##a=number(14)
##b=number(7)
##print(a+b)
##print(a-b)
##print(a*b)
##print(a/b)
##print(a%b)
##print(a==b)
##print(a<b)
##print(a>b)
     















































