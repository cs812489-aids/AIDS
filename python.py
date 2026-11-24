"""
print("hello world")

import sys
print(sys.version)

if 5 > 2:
print('Five is greater than two!')

x = 5
y = "Hello, World!"
print(x) #5
print(y) #Hello, World

print("Hello World!", end=" ")
print("I will print on the same line.")

print('Hello World!', end=' ')
print('I will print on the same line.')

print(3 + 3)
print(2 * 5)

print('I am', 35, 'years old.')

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 5.2
X = "John"
print(type(x))
print(type(y))

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


# unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # it gives space automatically

x = "Python"
y = "is"
z = "awesome"
print(x + y + z)

x = 5
y = 'bala'
print(x + y)

y = 'bala'
print(x , y)
x = 5

x = "awesome" # Global variable
def bala():
  print("Python is " + x)
bala()


# Function

x = "awesome"
def myfunc(z): # Z = Parameter
  y = "fantastic" # Local Variable
  print("Python is "+x +' '+y,z)
y=10
print("Python is ",x , y)
myfunc(7) # 7 = Argument


# Function With Default Parameter Value

def myfunc(z=10):
  print("Value is ",z)
myfunc(7)
myfunc()
myfunc(20)


# Function Calling From Another Function 

def fahrenheit_to_celsius(fahrenheit):
  return round( (fahrenheit - 32) * 5 / 9 ) # To Round The Decimal Value

print( fahrenheit_to_celsius(77), '°C')
print( fahrenheit_to_celsius(95), '°C')
print( fahrenheit_to_celsius(101), '°C')


# Function Assigning To A Variable 

def fahrenheit_to_celsius(fahrenheit):
  return round( (fahrenheit - 32) * 5 / 9 ) # To Round The Decimal Value
Temperature=fahrenheit_to_celsius(77)
print(Temperature, '°C')


# Function Without Definition

def riding():
 pass


# Function With Keyword Arguments

def my_function(age,animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name+' age is ',age)

my_function(name = "mani",age="5", animal = "dog")



# Function with Positional Only Arguments

def my_function(name,age, /):
  print("Hello", name)
  print("My Age", age)
my_function("Bala", 23)

def my_function(name,age):
  print("Hello", name)
  print("My Age", age)
my_function(age = 23 , name = "Bala")


def my_function(name, /): # Eror Because It Has Both Positional And Keyword Arguments
  print("Hello", name)
my_function(name = "Bala")


# Function with Keyword Only Arguments

def my_function(*,name,age):
  print("Hello", name)
  print("My Age", age)
my_function(age = 23 , name = "Bala")

def my_function(*,name,age): # Eror Because Parameter And Arguments Doesn't Match
  print("Hello", name)
  print("My Age", age)
my_function(23 , "Bala")


# Function with Combination Of Positional Only & Keyword Only Arguments

def my_function(name,age,/,*,bike,lap):
  print("Hello", name)
  print("My Age", age)
  print("My Bike", bike)
  print("My Lap", lap)
my_function("Bala" , 23 , lap = 'Asus' ,bike = 'MT 15')

def my_function(name,age,/,*,bike,lap):
  print("Hello", name)
  print("My Age", age)
  print("My Bike", bike)
  print("My Lap", lap)
my_function(name = "Bala" , 23 , lap = 'Asus' ,'MT 15')


# Funtion With List Arguments

def my_function(fruits):
  for fruit in fruits:
    print('fruit name is '+fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


# Funtion With Dictionary (Key : Value) Arguments

def my_function(person):
  print("My Name:", person["name"])
  print("My Age:", person["age"])
  print("My Bike:", person["bike"])
  print("type:", type(person)) # Type Keyword

my_person = {"name": "Bala", "age": 23, 'bike': 'MT 15'}
my_function(my_person)

# Function Returns A Tuple

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)


# Function Returns Values

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


# Function To Accept Arbitrary Arguments (Unknown Number Of Arguments)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Liya", "GUgan", "Yugan")


# Function To Accept Any Number of Positional Arguments

def pullaigo(*bala):
  print("Type:", type(bala)) # Type Keyword
  print("First argument:", bala[0])
  print("Second argument:", bala[1])
  print("All arguments:", bala)

pullaigo("Liya", "GUgan", "Yugan")


def my_function(*numbers):
  total = 2
  for bala in numbers:
    total *= bala
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


# Function with Combination Of Regular & Arbitrary (Positional) Arguments

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
  print("All data:", names)
my_function("Hello", "Liya", "GUgan", "Yugan")


# Program to find the largest & smallest number among the given numbers

def my_number(*numbers):
  if len(numbers) == 0:
    return None
  largest = numbers[0]
  smallest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
    if num < smallest:
      smallest = num
  return largest, smallest

print(my_number(3, 7, 2, 9, 1))


# Function To Accept Arbitrary (Positional) Keyword Arguments

def my_function(**friend):
  print("His name is " + friend["fname"] + " " + friend["lname"])

my_function(fname = "Karthick", lname = "Raja")


# Function To Accept Any Number of Keyword Arguments

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Bala", age = 30, city = "Chennai")


# Function with Combination Of Regular & Keyword Arguments

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
  for value in details.values():
    print( "value:", value)
  print("All data:", list(details.values()))  
  print("All data:", list(details.keys()))
  print("All data:", list(details.items()))
  print("All data:", details)
my_function("Bala123", age = 23, city = "Chennai", hobby = "Racing")


# Function with Combination Of Regular, Positional and Keyword Arguments


def my_function(Name, *Number, **Details):
  print("Name:", Name)
  print("Positional arguments:", Number)
  print("Keyword arguments:", Details)

my_function("Bala",25,30, city="chennai", country="Tamil Nadu")


# Function with Unpacking List or Tuple Arguments

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)



# Function with Unpacking Dictionary.


def my_function(fname, lname):
  return("Hello", fname, lname)

person = {"fname": "Karthick", "lname": "Raja"}
result = my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
print(result)
"""
#completed