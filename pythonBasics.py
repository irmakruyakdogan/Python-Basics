# Add two numbers with user input

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

sum = num2 + num1

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# Python Program to find the area of triangle

a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# Python program to swap two variables

x = 5
y = 10

# Python program to swap two variables

x = input('Enter value of x: ')
y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# Program to generate a random number between 0 and 50

import random

print(random.randint(0, 50))

# Program to Convert Kilometers to Miles

km = float(input("Enter value in kilometers: "))

conv_fac = 0.245345

miles = km * conv_fac
print('%0.2f km is equal to %0.2f miles' % (km, miles))

# Program to Convert Celsius To Fahrenheit

print("-" * 30)
print("1- Celsius to fahrenheit")
print("2- Fahrenheit to celsius")
print("-" * 30)

choice = input("Your choice (1/2): ")

if choice == "1":
    print("\n# Celsius to Fahrenheit")
    celsius = float(input("Degree to convert: "))
    fahrenheit = (celsius * 1.8) + 32
    print("{} degree celsius is equal to {} degree fahrenheit.".format(celsius, fahrenheit))
elif choice == "2":
    print("\n# Fahrenheit to Celsius")
    fahrenheit = float(input("Degree to convert: "))
    celsius = (fahrenheit - 32) / 1.8
    print("{} degree fahrenheit is equal to {} degree celsius.".format(fahrenheit, celsius))
else:
    print("Congratulations! You hacked the program.")


# Program to Check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# Program to Check if a Number is Odd or Even

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Program to Find the Largest Among Three Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# Program to Check Prime Number

num = int(input('Enter a number: '))

flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# Program to Find the Factorial of a Number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial = factorial * i
   print("The factorial of", num, "is", factorial)


# Program to Display the multiplication Table

num = int(input("Display multiplication table of? "))

for i in range(1, 11):
   print(num, 'x', i, '=', num * i)


# Program to Convert Decimal to Binary, Octal and Hexadecimal

dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")