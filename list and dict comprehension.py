#######list comprehension-----



##numbers=[i for i in range(1,6)]
##print(numbers)



##numbers=[i*i for i in range(1,6)]
##print(numbers)



##numbers=[i for i in range(1,6)if i%2==0]
##print(numbers)



##numbers=[i for i in range(1,6)if i%2!=0]
##print(numbers)



##numbers=[1,2,3,4,5]
##double=[i*2 for i in numbers]
##print(double)



##numbers=[1,2,3,4,5]
##result=[i for i in numbers if i>3]
##print(result)




##numbers=[i*5 for i in range(1,10)]
##print(numbers)



##numbers=[1,2,3,4,5]
##new=[i+10 for i in numbers]
##print(new)




##numbers=[i for i in range(1,21) if i>10]
##print(numbers)




##numbers=[i for i in range(1,31) if i%2==0 and i%3==0]
##print(numbers)




##numbers = [12, 5, 18, 7, 20, 3, 25]
##new=[i for i in numbers if i>10]
##print(new)




##numbers = [10, 15, 20, 25, 30, 35]
##new=[i for i in numbers if i%2==0]
##print(new)





##list=[i for i in range(1,101)if i%10==0]
##print(list)



##numbers = [-5, 10, -3, 20, -1, 30]
##new=[i for i in numbers if i>0]
##print(new)


##names=["ram","sam","jodu"]
##new=[i.upper()for i in names]
##print(new)


##words=["cat","python","java","code"]
##new=[len(i)for i in words]
##print(new)


##names=["rAm","Sam","joDu"]
##new=[i.lower()for i in names]
##print(new)


##numbers=[i*i for i in range(1,31) if i%2==0]
##print(numbers)




##numbers=[1,2,3,4,5]
##new=["even" if i%2==0  else "odd" for i in numbers]
##print(new)



##names=["rahul","akash","sudip","raj","ram"]
##new=[i for i in names if len(i)>4]
##print(new)


###dictionary comprehension-----




##dict={i:i for i in range(1,6)}
##print(dict)


##dict={i:i*i for i in range(1,6)}
##print(dict)


##names=["sankha","rahul"]
##x={i:len(i)for i in names}
##print(x)



##names={i:i for i in range(1,21) if i%2==0}
##print(names)


##names={i:i*i for i in range(1,21) if i%2!=0}
##print(names)


##marks={
##    "sankha":86,
##    "rahul":5,
##    "akash":88
##    }
##new={i:i for i in marks if marks[i]>50}
##print(new)



##marks={
##    "sankha":86,
##    "rahul":5,
##    "akash":88
##    }
##new={i:marks[i]+5 for i in marks}
##print(new)





##dict={i:"even" if i%2==0 else "odd" for i in range(1,11)}
##print(dict)




##marks={
##    "sankha":86,
##    "rahul":5,
##    "ash":88
##    }
##dict={i:i for i in marks if len(i)>4}
##print(dict)



















































