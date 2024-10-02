# To check whether a person is eligible for vote or not.

'''age = int(input("Enter your age as per aadhar : "))

if age >=18:
    print("Your'e eligible to vote")
else:
    print("Oops! you aren't eligible ")'''

# Check whether entered number by user is evev or odd.

'''num = int(input("Enter any number : "))

if num % 2 == 0:
    print(" It's even")
else:
    print("It's odd")'''

# Check the number is divisible by 7 or not

'''num = int(input("Enter any number : "))

if num % 7 == 0:
    print(" It's divisible by 7")
else:
    print("It's not divisible by 7")'''

# To Check the current bill per units

'''units = int(input(" Enter your consumed units : "))

if units <= 100 :
    print(" Your'e on line you got your current free")
if units > 100 and units <= 200 :
   d =  units - 100
   print(d*5)
if units >200 :
    de = units - 100
    print500+(de - 200)*10'''

# To check whether entered number or char  is 3 digits or 3 char are not

'''num = list(input("Enter number or char : "))

if num == num[0:1]:
    print("it is 1 digit")
elif num == num[0:2]:
    print("it is 2 digits")
elif num == num[0:3]:
    print("it is 3 digits")

else:
    print("you exceeded  3 digits ")'''

# To check whether entered char is palindrome or not

'''word = input("Enter any char : ")

if word[0] == word[-1]:
    print("It is palindrome")
else:
    print("No palindrome")'''

# To check whether entered number is prime or not

'''num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")'''
