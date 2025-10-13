#Recieve input from user
name=input("Enter your name: ")
print ("Hello " +  name)

#Type Conversiom

birth_year= input("Ënter your birth year: ")
age=2025-int(birth_year)
print(age)

#Additon of two numbers
First_num=float(input("Ënter first number: "))
Second_num=float(input("Enter second number: "))

Sum= First_num + Second_num
print("Sum: "+ str(Sum))

#Fun things with strings

course = "Python for beginners"
print(course.upper())
print(course.find('y'))
print(course.replace('for','4'))
print('Python' in course)
print('Java' in course)
print(course.title())

#Arithmetic operations
print(10/3)
print(10//3)
print(10%3)
print(10**3)

number=10
number+=3
number*=2
print(number)

#Operator precedence

print(10 + 3 * 2)
print((10 + 3) * 2)

#Comparison operators
x= 3==3
print(x)

price =5
print(price >19 and price <30)
print(price >19 or price <30)

#IF statements

temperature = 5
 
if temperature >30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature >20:
    print("It's a nice day")
else:
    print("It's a cold day")

#Exercise: Weight converter
Weight=float(input("Weight: "))
Unit= input ("(L)bs or (K)g: ")

if Unit.upper() == "L":
       converted = Weight/2.205
       print("Weight in kg: " + str(converted))
elif Unit.upper() == "K":
       converted = Weight * 2.205
       print("Weight in lbs: " + str(converted))
else:
         print("Invalid unit")
         