######lambda----


##square=lambda x:x*x
##print(square(5))



##add=lambda a,b:a+b
##print(add(10,20))



##cube=lambda x:x*x*x
##print(cube(5))



##maxium=lambda a,b:a if a>b else b
##print(maxium(6,5))




##even=lambda x:x%2==0
##print(even(6))



##maxium=lambda a,b,c: a if a>b and a>c else b if b>a and b>c else c
##print(maxium(8,6,7))



##check=lambda x:"positive" if x>0 else "negative" if x<0 else 0
##print(check(7))



##str=lambda x:len(x)
##print(str("python"))




##a=lambda x:x%10
##print(a(1234))



##compare=lambda a,b:"first" if a>b else "second" if b>a else "equal"
##print(compare(60,90))







####map()-----

##n=[1,2,3,4,5]
##result=map(lambda x:x*x,n)
##print(list(result))




##n=[1,2,3,4,5]
##result=map(lambda x:x*2,n)
##print(list(result))


##n=(1,2,3,4,5)
##result=map(lambda x:x*2,n)
##print(tuple(result))



##names=["sankha","rahul"]
##result=map(lambda x:x.upper(),names)
##print(list(result))


##n=[10,20,30]
##result=map(str,n)
##print(list(result))



##a=[1,2,3]
##b=[7,9,8]
##result=map(lambda x,y:x+y,a,b)
##print(list(result))



##numbers=[4,6,8]
##result=list(map(lambda x:x*2,numbers))
##print(result)




##a=[8,9]
##result=map(lambda x:x+10,a)
##print(list(result))




##c=[20,30,35,40]
##result=list(map(lambda c:c*9/5+32,c))
##print(result)




##a=[15,25,35,45]
##result=list(map(lambda a:(a+5)*(a+5),a))
##print(result)




##a=["10","20","30","40"]
##result=list(map(lambda a:int(a),a))
##print(result)










###filter()-----


##n=[1,2,3,4,5,6]
##result=list(filter(lambda n:n%2==0,n))
##print(result)




##n=[5,12,8,20,15,3]
##result=list(filter(lambda n:n>10,n))
##print(result)



##marks=[25,60,35,80,40,20]
##result=list(filter(lambda marks:marks>=40,marks))
##print(result)




##names=["amit","rahul","sourav","rohan"]
##result=list(filter(lambda names:len(names)>5,names))
##print(result)




##n=[-5,10,-2,8,-9,4]
##result=list(filter(lambda n:n<0,n))
##print(result)




















