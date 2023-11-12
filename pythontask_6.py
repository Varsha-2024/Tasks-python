#Arrays
fruit=["Apple","Banana","Oranage"]
print(fruit)

print(fruit[2])

fruit[1]="Cherry"
print(fruit)

f=len(fruit)
print(f)

fruit.append("Banana")
print(fruit)

for temp in fruit:
    print(temp)

fruit.sort(reverse=True)
print(fruit)

#User Input
name=input("please enter your name:")
age=input("please enter your age")
print(name)
print(age)
print("Thankyou")

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(num1+num2)

num3=float(input("Enter num1:"))
num4=float(input("Enter num2:"))
print(num3+num4)

username=input("Please enter your name:")
print("hi welcome",username)

try:
    print(digit)
except NameError:
    print("Digit is not defined,it is an error please check")

digit =5
try:
    print(digit)
except:
    print("Digit is  defined")

def add(n1,n2):
    try:
        print("please add:",n1+n2)
    except:
        print("We are sorry!!")
add(2,3)