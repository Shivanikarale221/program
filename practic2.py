
# Write a Python program to check whether a number is even or odd.

num=int(input("Enter your number"))
if num % 2==0:
    print("even")
else:
    print("odd")


# Write a program to find the largest of three numbers.

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))

if num1>=num2 and num1>=num3:
    print("num1 is largest")
elif num2>=num1 and num2>=num3:
    print("num2 is largest")
else:
    print("num3 is largest")


# Write a program to check whether a given number is prime.

num=int(input("Enter a number:"))

if num <=1:
    print("not a prime number")
else:
    for i in range(2,num):
        if num % i ==0:
            print("not a prime number")
            break
        else:
            print("prime number")


# Write a program to print the Fibonacci series up to n terms.

n=int(input("Enter the number of terms:"))
a=0
b=1

for i in range(n):
    print(a, end="")
    a,b=b, a+b


# Write a program to find the factorial of a number using a loop.

num=int(input("Enter a number:"))
factorial=1

for i in range(1,num+1):
    factorial=factorial*i

    print("factorial=",factorial)


# Write a program to reverse a string without using [::-1].

string=input("Enter a string:")
reverse=""
for i in string:
    reverse=i+reverse
    print("Reversed string:",reverse)


# Write a program to check whether a string is a palindrome.

string=input("Enter a string:")
reverse=""
for i in string:
    print("string is palindrome")
else:
    print("string is not palindrome")


# Write a program to count the number of vowels and consonants in a string.

string=input("Enter a string:")
vowels=0
consonants=0

for ch in string:
    if ch.lower() in "aeiou":
     vowels+=1
    elif ch.isalpha():
      consonants+=1

print("number of vowels:",vowels)
print("number of consonantas:",consonants)


# Write a program to find the sum of all elements in a list.

numbers=[20,20,20,20,20,20,20,20]

total=0

for num in numbers:
    total+=num
print("sum of all elements:",total)


# Write a program to find the largest and smallest element in a list without using max() or min().

number =[10,25,5,40,50]

largest=number[0]
smallest=number[0]

for num  in number:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num

print("largest element:",largest)
print("largest element:",smallest)


# Write a program to remove duplicate elements from a list.

number=[20,20,22,33,44,44]

unique=[]

for num in number:
    if num not in unique:
        unique.append(num)
    print("list after removing duplicates:",unique)


# Write a program to count how many times each element appears in a list using a diction

my_list=[1,2,2,3,1,4,2,3]

count={}

for item in my_list:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
    print(count)


# Write a program to find the second-largest number in a list.

numbers=[10,25,5,40,30]

largest=second=float()

for num in numbers:
    if num>largest:

     second=largest
     largest=num
    elif num>second and num!=largest:
       second=num
    print("second largest number:",second)


# Write a program to sort a list without using sort() or sorted().

numbers=[5,2,8,1,3]

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
         numbers[i],numbers[j]=numbers[j]=numbers[i]

print("Sorted list:",numbers)


# Write a function that accepts a list of numbers and returns a list containing only the even numbers.


def even_numbers(numbers):
    even=[]

    for num in numbers:
        if num %2==0:
            even.append(num)

        return even
    numbers=[1,2,3,4,5,6]

    print("Even numbers:",even_numbers(numbers))


# Write a program to find the frequency of each character in a string.

string=input("Enter a string:")

frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
    print("Character frequency:",frequency)


# Write a program to check whether two strings are anagrams of each other.

str1=input("Enter 1st string:")
str2=input("Enter 2nd string:")

if sorted(str1)== sorted(str2):
    print("stings are anagrams")
else:
    print("string are not anagrams")


# Write a program to find all duplicate values in a list.

numbers=[1,2,3,2,4,5,3,6,2]
duplicates=[]

for num in numbers:
    if numbers . count(num)>1 and num not in duplicates:
        duplicates.append(num)

    print("Duplicate values:",duplicates)


# Write a program that takes a sentence and finds the longest word.

sentence=input("Enter a sentence:")
words=sentence.split()
longest=""

for word in words:
    if len(word)>len(longest):
        longest=word

    print("longest word:",longest)


# Create a simple student marks program that:
# a. accepts marks for 5 subjects,
# b.calculates the total and percentage,
# c. assigns a grade,and displays whether the student passed or failed.


marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F"

if all(mark >= 35 for mark in marks):
    result = "Pass"
else:
    result = "Fail"

print("Total marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)