##1.write a program to print numbers from 1 to 10 using a for loop.

##i=1
##for i in range(1,11):
##    print(i)



##2.write a program to print numbers from 10 to 1 using a while loop.

##i=10
##while i>=1:
##    print(i)
##    i-=1



##3.write a program to print all even numbers from 1 to 50.

##i=2
##for i in range(2,51,2):
##    print(i)



##4.write a program to print all odd numbers from 1 to 50.

##i=1
##for i in range(1,51,2):
##    print(i)


##5.write a program to find the sum of numbers from 1 to 100.

##i=1
##sum=0
##for i in range(1,101):
##    sum+=i
##print(sum)



##6. take a number from the user and print its multiplication table from 1 to 10.

##n=int(input("the value of n is:"))
##i=1
##for i in range(1,n+1):
##    print(n*i)



##7. count how many numbers between 1 and 100 are divisible by 5.

##i=1
##count=0
##for i in range(1,101):
##    if(i%5==0):
##        count+=1
##print(count)


##8.take a number n from the user and print its first 10 multiplies.

##n=int(input("the value of n is:"))
##i=1
##for i in range(1,11):
##    print(n*i)



##9.print numbers from 1 to 100,but skip all numbers divisible by 3.
##
##i=1
##for i in range(1,101):
##    if(i%3==0):
##        continue
##    print(i)
      
    
    

##10.print numbers from 1 to 100 that are divisible by both 3 and 5.

##i=1
##for i in range(1,101):
##    if(i%3 ==0 and i%5==0):
##        print(i)



##11.count how many even numbers are present from 1 to 100.

##i=1
##count=0
##for i in range(1,101):
##    if(i%2==0):
##        count+=1
##print(count)




##12.take n from the user and find the sum of all even numbers from 1 to n.

##n=int(input("the value of n is:"))
##i=1
##sum=0
##for i in range(1,n+1):
##    if(i%2==0):
##        sum+=i
##print(sum)




##13.take a number from the user and calculate its factorial using a loop.

##n=int(input("the value of n is:"))
##i=1
##fact=1
##for i in range(1,n+1):
##    fact=fact*i
##print(fact)



##14.take a number from the user and print all of its factors.

##n=int(input("the value of n is:"))
##i=1
##for i in range(1,n+1):
##    if(n%i==0):
##        print(i)




##15.take n as input and print the square of every number from 1 to n.

##n=int(input("the value of n is:"))
##for i in range(1,n+1):
##    print(i*i)



##16.count how many digits are in a number.

##n=(input("n is:"))
##count=0
##for digit in str(n):
##         count=count+1
##print(count)
         
         


##17.print the sum of digits of a number.

##n=(input("n is:"))
##sum=0
##for digit in str(n):
##    sum=sum+int(digit)
##print(sum)



##18.reverse the number.

##n=(input("n is:"))
##reverse=""
##for digit in str(n):
##    reverse=digit+reverse
##print(reverse)




##19.check a number is palindrome or not.

##n=(input("n is:"))
##reverse=""
##for digit in str(n):
##    reverse=digit+reverse
##
##if(str(n)==reverse):
##    print("palindrome")
##else:
##    print("not")





##20.write to program to print the first 10 fibonacci numbers.

##a=0
##b=1
##for i in range(1,11):
##    print(a)
##    c=a+b
##    a=b
##    b=c



##21.print prime numbers from 1 to 20.

##for n in range(2,21):
##    count=0
##    for i in range(1,n+1):
##        if n%i==0:
##            count+=1   
##    if count==2:
##        print(n)





##22.check a number is prime or not.

##n=int(input("n is:"))
##count=0
##for i in range(1,n+1):
##    if(n%i==0):
##        count=count+1
##if count==2:
##    print("prime")
##else:
##    print("not prime")




####nested loop#####-----


##for i in range(1,3):
##    for j in range(1,3):
##        print(i,j)
        
    


##for i in range(1,3):
##    for j in range(1,3):
##        print("hello")



##for i in range(1,4):
##    for j in range(1,4):
##        print(i,j)




##for i in range(1,4):
##    for j in range(1,4):
##        print(i)




##for i in range(1,4):
##    for j in range(1,4):
##        print(j)




##for i in range(1,4):
##    for j in range(1,4):
##        print("hello")





##for i in range(1,4):
##    for j in range(1,3):
##        print(i,j)





##for i in range(1,4):
##    for j in range(1,3):
##        print(i)




##for i in range(1,4):
##    for j in range(1,3):
##        print(j)




##for i in range(1,4):
##    for j in range(1,3):
##        print("sankha ray")




##for i in range(1,3):
##    for j in range(1,4):
##        print("python")



##for i in range(2):
##    for j in range(4):
##        print(i,j)



##for i in range(1,4):
##    for j in range(1,i+1):
##        print(j)
##   




##for i in range(3):
##    for j in range(4):
##        print("hello")




##for i in range(2):
##    for j in range(5):
##        print("*")
##    



##for i in range(2):
##    for j in range(5):
##        print("***")
    


##for i in range(1,4):
##    for j in range(1,4):
##        print(i+j)



##for i in range(1,4):
##    for j in range(1,4):
##        print(i*j)



##for i in range(1,4):
##    for j in range(1,i+1):
##        print(i,j)                                                                                                                                       



##for i in range(1,4):
##    for j in range(1,i+1):
##        print(i)                                                                                                                                       




##for i in range(3):
##    for j in range(4):
##        print("*",end="")
##    print()

 



##for i in range(1,4):
##    for j in range(1,4):
##        print(i,end="")
##    print()




##for i in range(1,4):
##    for j in range(1,4):
##        print(j,end="")
##    print()




##for i in range(1,5):
##    for j in range(1,i+1):
##        print("*",end="")
##    print()




##for i in range(1,5):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()





##for i in range(1,5):
##    for j in range(1,5):
##        print(i,end="")
##    print()






##for i in range(1,5):
##    for j in range(1,i+1):
##        print(i,end="")
##    print()






##for i in range(1,6):
##    for j in range(1,6):
##        print(i,j,end="")
##    print()




##for i in range(1,11):
##    for j in range(1,11):
##        print(i,j,end="")
##    print()





##for i in range(4,0,-1):
##    for j in range(i):
##        print("*",end="")
##    print()





##for i in range(1,6):
##    for j in range(1,10):
##        print(i*j)





##sum=1
##for i in range(1,5):
##    for j in range(i):
##        print(sum,end="")
##        sum+=1
##    print()





##for i in range(1,11):
##    for j in range(1,11):
##        print(i*j,end="")
##    print()





##for i in range(1,5):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()





##for i in range(1,6):
##    for j in range(i):
##        print(i,end="")
##    print()





##for i in range(5,0,-1):
##    for j in range(1,i+1):
##        print(j,end="")
##    print()






























































