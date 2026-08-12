
# 1.Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even(n):
    if n% 2==0:
        return "even"
    else:
      return "odd"
print(is_even(7))

# 2.Largest of Two Numbers
# Write a function largest(a, b) that returns the larger number.

def largest(a,b):
 if a>b:
    return a
 elif  b > a:
     return b
 else:
    return f"not value found"
    
print(largest(22,55))
print(largest(100,44))

# 3.Print Numbers
# Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_number(n):
    for n in range(1,n+1):
        print(n)  

print(print_number(11))  

# 4.Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.

def sum_n(n):
    sum=0
    for i in range (1,n+1):
      sum+=i
    return sum
print(sum_n(4))
print(sum_n(10))


# 5.Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
table(5)

# 6.Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains Example:
# count_even([1, 2, 3, 4, 6])
# Output:3

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

print(count_even([1, 2, 3, 4, 5, 6]))


# 7.Find Maximum
# Without using max(), write a function that returns the largest number in a list.

def find_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_max([10, 25, 7, 40, 15]))

# 8.FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()


# 9.Palindrome Checker
# Write a function that returns True if a string is a palindrome.

def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("hello"))   

# 10.Count Vowels
# Write a function that counts the vowels in a string.
# Second Largest Number

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))


# 11.Second Largest Number
# Write a function that returns the second largest number in a list without using sort().

def second_largest(numbers):
    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

print(second_largest([10, 25, 40, 15, 30]))

# 12.Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct! You guessed it.")
            break
        elif guess < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

guessing_game()



# 14.Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95)) 
print(grade(82))  
print(grade(75))  
print(grade(65))  
print(grade(45))  






