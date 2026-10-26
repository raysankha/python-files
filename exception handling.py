##try:
##    a=10
##    b=0
##    print(a/b)
##except:
##    print("error occurred")




##try:
##    a=10
##    b=0
##    print(a/b)
##except ZeroDivisionError:
##    print("cannot divide by zero.")




##try:
##    a=x
##    b=5
##    print(a/b)
##
##except NameError:
##    print("x is not defined")




##try:
##    a=int(input("enter number:"))
##    b=int(input("enter number:"))
##    print(a/b)
##except ValueError:
##    print("please enter numbers only")
##except ZeroDivisionError:
##    print("cannot divide by zero")
    




##try:
##    a=6
##    b=0
##    print(a/b)
##except ZeroDivisionError:
##    print("cannot divide by zero")
##print("hello")





##try:
##    a=10
##    b=0
##    print(a/b)
##except Exception:
##    print("something went wrong")





##try:
##    print(10/0)
##except ZeroDivisionError as e:
##    print(e)



##try:
##    a=int(input("enter number:"))
##    b=int(input("enter number:"))
##    print(a/b)
##except ValueError as e:
##    print(e)





##try:
##    a=10
##    b=2
##    result=10/2
##except ZeroDivisionError:
##    print("cannot divide by zero")
##else:
##    print(result)



##try:
##    print(10/2)
##except ZeroDivisionError:
##    print("cannot divide by zero")
##finally:
##    print("program finished")




##try:
##    print(10/0)
##except ZeroDivisionError:
##    print("cannot divide by zero")
##finally:
##    print("program finished")




##print("hello")
##raise Exception("something went wrong")
##print("bye")



##try:
##    print("hello")
##    raise Exception("something went wrong")
##except Exception:
##    print("somehting went wrong")
##print("bye")




##balance=500
##if balance<1000:
##    raise Exception("balance too low")




##age=18
##if age<20:
##    raise Exception("age must be 20 or above")






##age=18
##try:
##    if age<20:
##        raise Exception("age must be 20 or above")
##except Exception:
##    print("age must be 20 or above")
##
##print("program is finished")





##age=18
##try:
##    if age<20:
##        raise Exception("age must be 20 or above")
##except Exception as e:
##    print(e)





##balance=5000
##amount=7000
##try:
##    if amount>balance:
##        raise Exception("insufficient balance")
##
##except Exception as e:
##    print(e)





##marks=25
##try:
##    if marks<40:
##        raise Exception("student failed")
##except Exception as e:
##    print(e)




##try:
##    age=int(input("age:"))
##    if age<18:
##        raise Exception("age must be 18 or above")
##except Exception as e:
##    print(e)





##try:
##    n1=int(input("n is:"))
##    n2=int(input("n is:"))
##    print(n1/n2)
##except ZeroDivisionError:
##    print("zero cannot be divided")
##
##except ValueError:
##    print("please enter numbers only")




##try:
##    n=int(input("n is:"))
##    numbers=[10,20,30,40]
##    print(numbers[n])
##
##except IndexError:
##    print("index is not present")





##try:
##    n1=int(input("n1 is:"))
##    n2=int(input("n2 is:"))
##    print(n1*n2)
##except ValueError:
##    print("put numbers only")




##try:
##     n=int(input("n is:"))
##     print(100/n)
##except ZeroDivisionError:
##    print("zero is not divided")
##except ValueError:
##    print("put only numbers")




##try:
##     n=int(input("n is:"))
##     print(10/n)
##except Exception:
##    print("something went wrong")
##finally:
##    print("program finished")




##try:
##    n=int(input("n is:"))
##    print(n*n)
##except Exception:
##    print("something went wrong")
##else:
##    print("calculation sucessfull")




##try:
##    n=int(input("n is:"))
##    list=[1,2,3,4,5]
##    print(list[n])
##
##except Exception:
##    print("something went wrong")




##try:
##    n1=int(input("n1 is:"))
##    n2=int(input("n2 is:"))
##    print(n1+n2)
##    print(n1-n2)
##    print(n1*n2)
##    print(n1/n2)
##except ValueError:
##    print("put only numbers")
##except ZeroDivisionError:
##    print("zero cannot be divided")




##try:
##    student={
##        "name":"sankha",
##        "marks":85
##        }
##    key=input("enter key:")
##    print(student[key])
##except KeyError:
##    print("key does not exists")





##try:
##    n=int(input("n is:"))
##    a=[1,2,3,4]
##    print(a[n])
##    x=5
##    y=n
##    print(x/y)
##except ValueError:
##    print("put only numbers")
##except IndexError:
##    print("index does not exists")
##except ZeroDivisionError:
##    print("zero is not divided")
##    
    
    


##try:
##     n=int(input("n is:"))
##     if (n<=0):
##          raise Exception("number must be positive")
##except Exception as e:
##     print(e)
##     
     
    


##try:
##     marks=int(input("marks is:"))
##     if marks<0 or marks>100:
##          raise Exception("invalid marks")
##except Exception as e:
##     print(e)




##try:
##     passowrd=input("passowrd is:")
##     if len(passowrd)<6:
##          raise Exception("passowrd too short")
##     print("passowrd is valid")
##except Exception as e:
##     print(e)



##try:
##     n=int(input("n is:"))
##     if n%2!=0:
##          raise Exception("number must be even")
##except Exception as e:
##     print(e)
          



##try:
##     n1=int(input("n1 is:"))
##     n2=0
##     if n2==0:
##          raise Exception ("cannot divide by zero")
##     print(n1/n2)
##except Exception as e:
##     print(e)
##                   





##try:
##     withdrawal_amount=int(input("withdrawal_amount is:"))
##     balance=5000
##     if withdrawal_amount>balance:
##          raise Exception("insufficient balance")
##except Exception as e:
##     print(e)






##try:
##     temp=int(input("temp is:"))
##     if temp<-50 or temp>60:
##          raise Exception("invalid temparature")
##except Exception as e:
##     print(e)





##try:
##   username=input("username is:")
##   if len(username)<3:
##        raise Exception("invalid username")
##except Exception as e:
##     print(e)
##   
   


##try:
##     n=int(input("n is:"))
##     if n>100:
##          raise Exception("number is too large")
##except Exception as e:
##     print(e)



##
##try:
##     email=input("email is:")
##     if "@" not in email:
##          raise Exception("invalid email")
##except Exception as e:
##     print(e)




##try:
##     shopping_amount=int(input("shopping_amount is:"))
##     if shopping_amount<=0:
##          raise Exception("should be positive")
##except Exception as e:
##     print(e)
##          




##class AgeError(Exception):
##    pass
##try:
##    age=int(input("age is:"))
##    if age<18:
##        raise AgeError("age must be 18 or above")
##    print("eligible")
##except AgeError as e:
##    print(e)




##try:
##    marks=int(input("marks is:"))
##    if marks<0 or marks>100:
##        raise Exception("invalid marks")
##    print("valid marks")
##except Exception as e:
##    print(e)





##class MarkError(Exception):
##    pass
##try:
##    marks=int(input("marks is:"))
##    if marks<0 or marks>100:
##        raise MarkError("invalid marks")
##    print("valid marks")
##except MarkError as e:
##    print(e)






##class NegativeNumber(Exception):
##    pass
##try:
##    number=int(input("number is:"))
##    if number<0:
##        raise NegativeNumber("number will be negative")
##    print("positive number")
##except NegativeNumber as e:
##    print(e)





##class PasswordError(Exception):
##    pass
##try:
##    password=input("password")
##    if len(password)<6:
##        raise PasswordError("invalid password")
##    print("valid password")
##except PasswordError as e:
##    print(e)





##class InsufficientBalanceError(Exception):
##    pass
##try:
##    withdrawal_amount=int(input("withdrawal_amount is:"))
##    balance=5000
##    if  withdrawal_amount>balance:
##        raise InsufficientBalanceError("balance is too low")
##    print("withdraw sucessfully")
##except InsufficientBalanceError as e:
##    print(e)





##class InvalidTemperatureError(Exception):
##    pass
##try:
##    temperature=int(input("temperature is:"))
##    if temperature<-50 or temperature>60:
##        raise InvalidTemperatureError("temperature is invalid")
##    print("valid temperature")
##except InvalidTemperatureError as e:
##    print(e)




##class InvalidAgeError(Exception):
##    pass
##
##class InvalidMarksError(Exception):
##    pass
##try:
##    age=int(input("age is:"))
##    if age<0:
##        raise InvalidAgeError("age is invalid")
##    print("valid age")
##
##except InvalidAgeError as e:
##    print(e)
##try:
##    marks=int(input("marks is"))
##    if marks<0 or marks>100:
##        raise InvalidMarksError("invalid marks")
##    print("valid marlks")
##except InvalidMarksError as e:
##    print(e)





##
##class InvalidPinError(Exception):
##    pass
##class InsufficientBalanceError(Exception):
##    pass
##class InvalidAmountError(Exception):
##    pass
##correct_pin=722136
##try:
##    pin=int(input("pin is:"))
##    if pin!=correct_pin:
##        raise InvalidPinError("put wrong pin")
##    print("correct pin")
##except InvalidPinError as e:
##    print(e)
##try:
##    amount=int(input("amount is:"))
##    if amount<=0:
##        raise InvalidAmountError("invalid amount")
##except InvalidAmountError as e:
##    print(e)
##try:
##    balance=int(input("balance is:"))
##    if amount>balance:
##        raise InsufficientBalanceError("insufficient balance")
##    print("withdrawal succesfull")
##except  InsufficientBalanceError as e:
##    print(e)


















































































































































