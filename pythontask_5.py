#List
vegies=["Carrot","Beetroot","Potato"]
print(vegies)
print(type(vegies))

for i in vegies:
    print(i)

for i in vegies:
    print(i,end=" ")

print(vegies[2])

vegies.append("Cabbage")
print(vegies)

vegies.insert(2,"tomato")
print(vegies)
print(len(vegies))

vegies.sort()
print(vegies)

vegies.sort(reverse=True)
print(vegies)


#Tuple
fruits=("apple","banana","cherry")
print(fruits)
print(type(fruits))

temp=list(fruits)
print(temp)
print(type(temp))

temp.append("Berry")

temp=tuple(temp)
print(temp)
print(type(temp))

print(len(temp))
print(temp[1])

fruits1=("Orange","grapes")
print(fruits +fruits1)

#set
fruits={"apple","banana","cherry"}
print(fruits)
print(type(fruits))

fruits.remove("banana")
print(fruits)
print(len(fruits))

for x in fruits:
    print(x)

print("apple" in fruits)

fruits.add("banana")
print(fruits)

#Dict
student={
    "name":"varsha",
    "Age":24,
    "Roll NO":2
}
print(student)
print(type(student))

student.pop("Roll NO")
print(student)

student["DOB"]=1999
print(student)

for temp in student:
    print(temp)

for temp1,temp2 in student.items():
    print(temp1,temp2)