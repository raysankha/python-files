##with open("data.txt","w")as file:
##    file.write("banana")




##with open("data.txt","r")as file:
##    print(file.read(3))
##    print(file.tell())




##with open("data.txt","r")as f:
##    f.seek(2)
##    print(f.read(2))




##with open("data.txt","r")as f:
##    print(f.readline().strip())



    
##with open("data.txt","r")as f:
##    f.read(2)
##    f.seek(4)
##    print(f.read(1))
##    print(f.tell())




##with open("students.txt","w")as f:
##    f.write("sankha ray")
##    f.write("\nrahul mukherjee")
##
##with open("students.text","a")as f:
##    f.write("python")
##
##with open("students.text","r")as f:
##    print(f.read())




##with open("students.text","r")as f:
##    for i in f:
##        print(i.strip())
        





##with open("students.text","w")as f:
##    f.write("sankha")
##    f.write("\n21")
##    f.write("\ncse")
##with open("students.text","a")as f:
##    f.write("\npython devoloper")
##with open("students.text","r")as f:
##    print(f.read())




##with open("students.text","r")as f:
##    for i in f:
##        print(i.strip())







##with open("students.text","w")as f:
##    f.write("sankha")
##    f.write("\n21")
##    f.write("\ncse")
##with open("students.text","a")as f:
##    f.write("\npython devoloper")
##with open("students.text","r")as f:
##    print(f.readlines())






##with open("students.text","w")as f:
##    f.writelines(["sankha","\ncse","\ndurgapur"])
##with open("students.text","a")as f:
##    f.write("\npython devoloper")
##with open("students.text","r")as f:
##    print(f.read())





##with open("students.text","w")as f:
##    f.write("1 sankha")
##    f.write("\n2 21")
##    f.write("\n3 cse")
##with open("students.text","a")as f:
##    f.write("\n4 python devoloper")
##with open("students.text","r")as f:
##    print(f.read())




##count=0
##with open("students.text","r")as f:
##    for i in f:
##        count+=1
##print(count)





##with open("students.text","w")as f:
##    f.write("10")
##    f.write("\n20")
##    f.write("\n30")
##with open("students.text","a")as f:
##    f.write("\n40")
##with open("students.text","r")as f:
##    print(f.read())
##
##sum=0
##with open("students.text","r")as f:
##    for i in f:
##        sum+=int(i)
##print(sum)





##with open("students.text","w")as f:
##    f.write("py")
##    f.write("\njava")
##    f.write("\nc++")
##with open("students.text","a")as f:
##    f.write("\nhtml")
##with open("students.text","r")as f:
##    print(f.read())



##with open("students.text","r")as f:
##    for i in f:
##        print(i.upper())






##with open("students.text","r")as f:
##    for i in f:
##        if int(i)%2!=0:
##            print(i.strip())



##with open("student.txt","r")as file:
##    for i in file:
##        print(len(i.strip()))





##with open("student.text","w")as f:
##    f.write("python\nis\neasy")
##with open("student.text","r")as f:
##    print(f.read())
##







##with open("students.text","r")as f:
##    for i in f:
##        if int(i)>20:
##            print(i.strip())







##with open("students.txt","w")as f:
##    f.write("python")
##
##with open("students.txt","r")as f:
##    print(f.tell())





##with open("students.txt","w")as f:
##    f.write("hello world")
##with open("students.txt","r")as f:
##    print(f.read(4))
##    print(f.tell())




##with open("students.txt","w")as f:
##    f.write("python programming")
##with open("students.txt","r")as f:
##    print(f.read(6))
##    f.seek(0)
##    print(f.read())




##with open("students.txt","w")as f:
##    f.write("abcdefghu")
##with open("students.txt","r")as f:
##    f.seek(4)
##    print(f.read())





##with open("student.txt", "w") as file:
##    file.write("ABCDEFG")
##
##with open("student.txt", "r") as file:
##    file.read(3)
##    print(file.tell())





##with open("student.txt", "w") as file:
##    file.write("Python")
##
##with open("student.txt", "r") as file:
##    file.seek(2)
##    print(file.read(3))





##with open("student.txt", "w") as file:
##    file.write("Programming")
##
##with open("student.txt", "r") as file:
##    file.read(5)
##    file.seek(1)
##    print(file.read(4))
##    print(file.tell())




##with open("student.txt","w")as file:
##    file.write("0123456789")
##with open("student.txt","r")as file:
##    file.seek(5)
##    print(file.read())
    



##with open("student.txt","w")as file:
##    file.write("python is easy")
##
##with open("student.txt","r")as file:
##    print(file.read(6))
##    print(file.tell())
##    file.seek(0)
##    print(file.read())





####json###----



##import json
##student={
##    "name":"rahul",
##    "age":20,
##    "marks":25
##    }
##with open("student.json","w")as f:
##    json.dump(student,f)







##import json
##with open("student.json","r")as f:
##    data=json.load(f)
##print(data)






##import json
##student={
##    "name":"rahul",
##    "age":20,
##    "marks":25
##    }
##data=json.dumps(student)
##print(data)
##print(type(data))






##import json
##student='{"name":"rahul","age":20,"marks":25}'
##data=json.loads(student)
##print(data)
##print(type(data))






##import json
##student='{"name":"rahul","marks":75}'
##data=json.loads(student)
##print(data["name"])
##print(data["marks"])
##print(type(data))





##import json
##data='{"name":"rahul","age":20}'
##print(json.loads(data))





##import json
##student={
##    "name":"sankha",
##    "roll_no":66,
##    "marks":74
##    }
##data=json.dumps(student)
##print(data)
##print(type(data))
##student='{"name":"sankha","roll_no":66,"marks":74}'
##data=json.loads(student)
##print(data)
##print(type(data))





##import json
##student={
##    "sankha":75,
##    "rahul":66,
##    "akash":74
##    }
##with open("student.json","w")as f:
##    json.dump(student,f)
##
##with open("student.json","r")as f:
##    data=json.load(f)
##print(data)    





##import json
##student='{"name":"raj","salary":25000}'
##data=json.loads(student)
##print(type(data))
##data["salary"]=30000
##print(data)





##import json
##student={"name":"raj","salary":25000}
##print(json.dumps(student,indent=4))








##import json
##student={
##    "marks":75
##    }
##with open("student.json","w")as f:
##    json.dump(student,f)
##
##with open("student.json","r")as f:
##    data=json.load(f)
##
##if student["marks"]>40:
##    print("pass")
##else:
##    print("fail")
##print(data)






##import json
##student={
##    "sankha":75,
##    "rahul":66,
##    "akash":74
##    }
##with open("student.json","w")as f:
##    json.dump(student,f)
##
##with open("student.json","r")as f:
##    data=json.load(f)
##data["city"]="kolkata"
##print(data)







##import json
##student=[
##    {"name":"sankha","marks":70},
##    {"name":"rahul","marks":75},
##    {"name":"akash","marks":66}
##    ]
##    
##with open("student.json","w")as f:
##    json.dump(student,f)
##
##with open("student.json","r")as f:
##    data=json.load(f)
##
##max=data[0]
##for i in data:
##    if i["marks"]>max["marks"]:
##        max=i
##print(max["name"])







##try:
##    import json
##    data="{'name':'rahul'}"
##    student=json.loads(data)
##    print(student)
##except json.decoder.JSONDecodeError:
##    print("program does not run")






##import json
##data='{"name": "Sankha", "age": 20, "city": "Durgapur"}'
##student=json.loads(data)
##print(student)





##import json
##student = {
##    "name": "Rahul",
##    "marks": 85,
##    "passed": True
##}
##data=json.dumps(student)
##print(data)







##import json
##
##data = '{"name": "Sankha", "marks": 90, "city": "Bankura"}'
##student=json.loads(data)
##print(student["marks"])






##student = {
##    "name": "Aman",
##    "age": 21,
##    "marks": 88
##}
##with open("student.txt","w")as f:
##    json.dump(student,f)





##with open("student.txt","r")as f:
##    data=json.load(f)
##    print(data)









###OS###------

#1.current kis folder me kaam chal raha he vo dekhna.

##import os
##print(os.getcwd())




#2.current folder ke andar maujood files aur folders ka naam ki list deta hai.

##import os
##print(os.listdir())




#3.koi speicific folder ki list dekhni ho to.

##import os
##print(os.listdir("C:/Users/raysa/OneDrive/Dokumen"))





#4.file delete karna

##import os
##os.remove("hggh.py")





#5.file ya folder ka name badalna

##import os
##os.rename("agrs and kwargs.py","args and kwargs.py")




#6.path exists karta he ya nhi

##import os
##print(os.path.exists("student.txt"))






#7.naya folder banana

##import os
##os.mkdir("javafolder")





#8.nested folder banana

##import os
##os.makedirs("java/course/day1")






#9.path banana

##import os
##path = os.path.join("PythonFolder", "student.txt")
##print(path)





#10.kya ye folder hai

##import os
##print(os.path.isdir("pythonfolder"))





#11.kya ye file hai

##import os
##print(os.path.isfile("args and kwargs.py"))





#12.empty folder delete karne ke liye

##import os
##os.mkdir("sankha")
##os.rmdir("sankha")





#13.file ka size

##import os
##print(os.path.getsize("student.txt"))





#14.extension alag karna

##import os
##print(os.path.splitext("student.txt"))




#15.current folder change karna

##import os
##os.chdir("maths")
##print(os.getcwd())





import os
os.rmdir("xfolder")






































































































