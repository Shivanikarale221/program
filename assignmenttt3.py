#data type.

#Find the data type of every value in a mixed list.

# my_list=[5,6,7,"shivani","pune",39.4,True,'s']
# print(type(my_list))
# for i in  my_list:
#     print(i,"=",type(i))


# Convert a nested list into a tuple of tuples.

# my_list=[[1,2],[3,4],[5,6],[7,8]]
# result=tuple(tuple(x)for x in my_list)
# print(result)


# Remove all duplicate values from a mixed list while preserving the original order.

# my_list=[1,"apple",2,1,"apple",3,2,True]
# result=[]
# for value in my_list:
#     if value not in result:
#         result.append(value)

# print(result)


# 2. Operators

# Check whether a number is a power of 2 using operators.

# n=int(input("enter a number:"))
# if n > 0 and (n &(n-1))==0:
#     print("power of 2")
# else:
#     print("not a power of 2")65


# Swap two numbers using bitwise XOR.4

# a=40
# b=80

# a=a^b
# b=a^b
# a=a^b

# print("a=",a)
# print("b=",b)


# Find whether a number is divisible by both 4 and 6 using logical operators.


# n = int(input("Enter a number: "))

# if n % 4 == 0 and n % 6 == 0:
#     print("Divisible by both 4 and 6")
# else:
#     print("Not divisible by both 4 and 6")



# Calculate the total electricity bill using different unit rates.


# units = int(input("enter units:"))

# if units <= 100:
#     bill=units*5

# elif units <=200:
#     bill=(100*5)+((units-100)*7)

# else:
#     bill=(100*5)+(100*7)+((units-200)*10)

# print("Electricity Bill=",bill)

                

# 3. Conditional Statements

# Check whether three sides can form a triangle.

# a=int(input("enter first side:"))
# b=int(input("enter second side:"))
# c=int(input("enter third side:"))

# if a+b>c and a+c>b and b+c>a:
#     print("the sides can from a tiangle")
# else:
#     print("the side can not from a triangle")



# Determine the type of triangle (Equilateral, Isosceles, Scalene).


# a=int(input("enter first side:"))
# b=int(input("enter second side:"))
# c=int(input("enter third side:"))

# if a==b and b==c:
#     print("Equilateral Tringle")
# elif a==b or b==c or c==a:
#     print("Isosceles Tringle")
# else:
#     print("Scalene")




# Create a simple ATM menu (Withdraw, Deposit, Balance).

# print("1.withdraw")
# print("2.Depodit")
# print("3.Balance")

# choice=int(input("Enter your choice:"))

# if choice==1:
#     amount=int(input("Enter a amount to withdraw:"))

# if amount<=balance:
#       balance=balance-amount
#       print("withdrawal successful")
#       print("Remaming balance:",balance)
#     else:
#      print("insufficient balance")

# elif choice == 2:
# amount= int(input("Enter amount to deposit:"))
# balance=balance + amount
# print("Deposit successful")
# print("New balance:",balance)

# elif choice ==3:
# print("your balance is:",balance)

# else:
# print("Invalid choice")




# Calculate income tax based on different tax slabs.


# income=int(input("Enter your annual income:"))

# if income <= 250000:
#     tax=0

# elif income <= 500000:
#     tax=(income-250000)*5/100

# elif income <= 1000000:
#     tax=(250000*5/100) + (500000*20/100)

# else:
#     tax=(250000*5/100) + (500000*20 / 100) + ((income-1000000)* 30 / 100)

# print("income tax=",tax)




# Create a menu-driven calculator using if-elif.


# a= float(input("Enter first number:"))
# b=float(input("Enter second number:"))

# print("1.addtion")
# print("2.subtraction")
# print("3.multiplication")
# print("4.division")

# choice=int(input("Enter your choice:"))

# if choice == 1:
#     print("Result =",a+b)

# elif choice == 2:
#     print("Result=",a - b)

# elif choice == 3:
#     print("Result=",a * b)

# elif choice == 4:
#  if b!=0:
#     print("Result=",a / b)
# else:
#    print("cannot divide by zero")

 # print("Invalid choice")



# 4. Loops

# Print all prime numbers between 1 and n.

# n = int(input("Enter n:"))

# for num in  range(2,n + 1):
#     is_prime = True

#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#       print(num)



# Find the factorial of a number using a loop.

# n = int(input("Enter a number:"))

# factorial = 1

# for i in range(1,n+1):
#     factorial=factorial*i

# print("factorial=",factorial)




# Print the Fibonacci series up to n terms.


# n=int(input("Enter number of terms:"))

# a=0
# b=1

# for i in range(n):
#     print(a,end="")
#     a,b=b,a+b




# Check whether a number is an Armstrong number.

# n = int(input("Enter a number: "))

# temp = n
# sum = 0
# digits = len(str(n))

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** digits
#     temp = temp // 10

# if sum == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")




# Reverse a number and check if it is a palindrome.

# n = int(input("Enter a number: "))

# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print("Reverse =", reverse)

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# Find the Greatest Common Divisor (GCD) of two numbers


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# while b != 0:
#     a, b = b, a % b
# print("GCD =", a)


# 5. Functions

# Write a function to check if a string is a palindrome.

# def is_palindrom(s):
#     return s==s[::-1]

# text = input("Enter a string:")

# if is_palindrom(text):
#     print("palindrome")
# else:
#     print("Not a palindrome")


# Write a function to count vowels and consonants in a string.

# def count_vowels_consonants(s):
#     vowels = 0
#     consonants = 0

#     for ch in s.lower():
#         if ch in "aeiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1

#     return vowels, consonants

# text = input("Enter a string: ")

# v, c = count_vowels_consonants(text)

# print("Vowels:", v)
# print("Consonants:", c)
    


# Create a function to calculate simple and compound interest.

# def calculate_interest(p,r,t):
#     simple_interst=(p*r*t)/100
#     compound_interest=p*(1+r/100)**t-p
#     return simple_interst,compound_interest

# p = float(input("Enter principal:"))
# r = float(input("Enter Rate:"))
# t = float(input("Enter Timel:"))
# si,ci = calculate_interest(p,r,t)

# print("simple Interest:",si)
# print("compound interest:",ci)



# Write a function to return all factors of a number.

# def factors(n):
#     result=[]
#     for i in range(1,n+1):
#         if n % i==0:
#             result.append(i)

#     return result 

# num=int(input("Enter a number:"))
# print("Factors:",factors(num))


# Write a function to find the second-largest number in a list.

# def second_largest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[-2]


# numbers = [10, 20, 5, 30, 15]

# print("Second largest number:", second_largest(numbers))



# 6. Lists 

# Merge two lists without duplicates.

# def merge_lists(list1,list2):
#     return list(set(list1+list2))

# list1=[1,2,3,4,]
# list2=[6,7,8,9,10]
# print("Merged list:",merge_lists(list1,list2))


# Find the second-largest and second-smallest elements.

# def second_largest_smallest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()

#     second_smallest = unique_numbers[1]
#     second_largest = unique_numbers[-2]

#     return second_largest, second_smallest

# numbers = [10, 20, 5, 40, 15]

# largest, smallest = second_largest_smallest(numbers)

# print("Second largest:", largest)
# print("Second smallest:", smallest)



# Rotate a list to the left by k positions.

# def rotate_left(lst, k):
#     k = k % len(lst)
#     return lst[k:] + lst[:k]

# numbers = [1, 2, 3, 4, 5]
# k = 2

# print("Rotated list:", rotate_left(numbers, k))


# Separate even and odd numbers into two lists.

# def separate_even_odd(numbers):
#     even = []
#     odd = []

#     for n in numbers:
#         if n % 2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)

#     return even, odd
# numbers = [1, 2, 3, 4, 5, 6]
# even, odd = separate_even_odd(numbers)
# print("Even:", even)
# print("Odd:", odd)


# Find the common elements between two lists.

# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))


# list1 = [1, 2, 3, 4, 5,11,10,12,13,]
# list2 = [3, 4, 5, 6, 7,11,12,13,10,12,14]

# print("Common elements:", common_elements(list1, list2))

# 7. Tuples & Sets

# Count the frequency of each element in a tuple.

# def count_frequency(t):
#     frequency = {}

#     for item in t:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1

#     return frequency

# t = (1, 2, 2, 3, 3, 3, 4)
# print("Frequency:", count_frequency(t))



# Find the union, intersection, and difference of two sets.

# def set_operations(set1, set2):
#     union = set1 | set2
#     intersection = set1 & set2
#     difference = set1 - set2
#     return union, intersection, difference
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# u, i, d = set_operations(set1, set2)

# print("Union:", u)
# print("Intersection:", i)
# print("Difference:", d)


# Check whether one set is a subset of another.

# def is_subset(set1, set2):
#     return set1.issubset(set2)
# set1 = {1, 2}
# set2 = {1, 2, 3, 4}
# if is_subset(set1, set2):
#     print("Set 1 is a subset of Set 2")
# else:
#     print("Set 1 is not a subset of Set 2")


# 8. Dictionaries

# Count the frequency of words in a sentence.

# sentence=input("Enter a sentence:")
# words = sentence.split()
# frequency={}

# for word in words:
#     frequency[word]=frequency.get(word,0)+1

# print("word frequency:")
# for word, count in frequency.items():
#     print(word,":",count)


# Create a dictionary from two lists (keys and values).

# keys=["name","age","city"]
# values=["shivani","21","akola"]
# dictionary=dict(zip(keys,values))
# print(dictionary)


# Sort a dictionary by its values.

# data={"a":3,"b":1,"c":4,"e":2,"f":5}
# sorted_data=dict(sorted(data.items(),key=lambda x: x[1]))

# print(sorted_data)



# 9.File Handling

# Read a text file and count the number of lines, words, and characters.

# file=open('myfile.txt','r')

# text=file.read()

# lines=text.splitlines()
# words=text.split()
# char=len(text)

# print("number of lines:",len(lines))
# print("number of words:",len(words))
# print("number of charecter:",char)
# file.close()



# Copy only the even-numbered lines from one file to another.

# source=open("study.txt","r")
# destination=open("even_lines.txt","w")

# lines=source.readline()

# for i in range(1,len(lines),2):
#     destination.write(lines[i])

# source.close()
# destination.close()

# print("Even-numberred lines copie successfully.")


# 10. Exception Handling

# Handle invalid integer input using try-except.

# try:
#     num=int(input("Enter an integer:"))
#     print("you entered:",num)

# except ValueError:
#     print("Invalid input! please enter an integee.")


# Handle file-not-found errors while reading a file.

# try:
#     file=open("study.txt","r")
#     text=file.read()
#     print(text)
#     file.close()

# except FileNotFoundError:
#     print("File not found!")


# 11. Modules

# Create a random password generator using the random and string modules.

import random
import string

length=int(input("Enter passwpord lenght:"))
characters=string.ascii_letters+string.digits+string.punctuation

password=""

for i in range(length):
    password+=random.choice(characters)

print("Random password:",password)



# Use the datetime module to calculate the number of days between two dates.

