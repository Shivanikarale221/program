# 1. Check if a number is positive, negative, or zero.

# num=int(input("Enter your number"))
# if num>0:
#   print("positive")
# elif num<0:
#   print("negetive")
# else:
#   print("zero")


# 2. Check whether a number is even or odd.

# num=int(input("enter a number"))
# if num % 2==0:
#     print("even")
# else:
#     print("odd")


# 3.Find the greater of two numbers.

# num=int(input("Enter your 1st number : "))
# num2=int(input("Enter your 2nd number : "))

# if num>num2:
#     print(num,"is a gretest number ...")
# elif num2>num:
#     print ("The gretest number is num2 :",num2)  
# else:
#     print("Invalid number...")      

# 4. Find the greatest of three numbers.

# num1=int(input("Enter 1st number :"))
# num2=int(input("Enter 2nd number:"))
# num3=int(input("Enter 3rd number:"))

# if num1>num2 and num1>num3  :
#     print("num3 is gretest number..")
# elif num2>num1 and num2>num3 :
#     print("num2 is greater number" )
# elif num3>num2 and num3>num1 :
#     print("num3 is greater number")
# else:
#     print("None of these are greater... ")


# 5.Check if a person is eligible to vote (age ≥ 18).

# num=int(input("Enter your age"))
# if num >=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible for vote")


# 6.Check whether a year is a leap year.

# num=int(input("Enter your year: "))
# if num % 4==0:
#     print("this is leap year")
# else:
#     print("this s not leap year")


# 7.Check if a character is a vowel or consonant.

# ch=input("Enter a character:")
# if ch.lower() in "aeiou":
#     print("vowel")
# else:
#   print("constant")


# 8.Check whether a number is divisible by 5 and 11.

# num=int(input("Enter a nunmber"))
# if num % 5==0 and num % 11 ==0:
#     print("the number divided by 5 and 11")
# else:
#     print("the number not divided by 5 and 11")


# 9.Check if a number is a multiple of both 3 and 7.

# num=int(input("Enter a number"))
# if num % 3==0 and num % 7==0:
#     print("the numbre multiple by 3 and 7")
# else:
#     print("the number not multiple by 3 and 7")


# 10.Assign grades based on marks:

# num=int(input("Enter marks"))
# if num >90 :
#     print("you have A grade")
# elif num >80:
#     print("you have B grade")
# elif num >70:
#     print("you have C grade")
# else:
#     print("you are faill")


# 11. Check if a character is uppercase or lowercase.

# ch=input("Enter character")
# if ch.isupper():
#     print("uppercase")
# elif ch.islower():
#     print("lowercase")
# else:
#     print("not an alphabete")


# 12. Find whether the entered alphabet is a vowel using if-elif.

# ch=input("Enter an alphabet:")
# if ch=='a' or ch=='A':
#     print("vowel")
# elif ch=='e' or ch=='E':
#     print("vowel")
# elif ch== 'i' or ch=='I':
#     print("vowel")
# elif ch== 'o' or ch=='O':
#     print("vowel")
# elif ch== 'u' or ch=='U':
#     print("vowel")
# else:
#     print("consont")



# 13. Check if three sides can form a triangle.

# a=float(input("Enter a 1st side"))
# b=float(input("Enter a 2nd side"))
# c=float(input("Enter a 3rd side"))
 
# if a+b>c and a+c>b and b+c>a:
#     print(" the side can from a triangle")
# else:
#     print("the side cannot from a tringle")


# 14. Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a=float(input("Enter 1st side:"))
# b=float(input("Enter 2nd side:"))
# c=float(input("Enter 3rd side:"))

# if a==b and b==c :
#     print("Equilateral")
# elif a==b or b==c or a==c :
#     print("Isosceles")
# else:
#     print("scalene")




# 15. Find the largest among four numbers.

# a=int(input("Enter 1st number"))
# b=int(input("Enter 2nd number"))
# c=int(input("Enter 3rd number"))
# d=int(input("Enter 4th number"))

# if a>=b and a>c and a>=d:
#     print("a is largest ")
# elif b>=a and b>=c and b>=d:
#     print("b is largest")
# elif c>=a and c>=b and c>=d:
#     print("c is largest")
# else:
#     print("d is largest")


# 16. Check whether a number is a three-digit number.

# num=int(input("Enter your number"))
# if 100<= num <= 999:
#     print(" this is three digit number")
# else:
#     print("this is not three digit number")


# 17. Calculate electricity bill using slab rates.

# units=int(input("Enter electricity units:"))

# if units<=100:
#     bill=units*5
# elif units <=200:
#     bill=(100*5)+(units-100)*7
# elif units <=300:
#     bill=(100*5)+(100*7)+(units-200)*10
# else:
#     bill=(100*5)+(100*7)+(100*10)+(units-300)*12
# print("Electricity bill=",bill)



# 18. Calculate income tax based on income slabs.

# income = float(input("Enter your annual income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = income * 0.05
# elif income <= 1000000:
#     tax = income * 0.20
# else:
#     tax = income * 0.30

# print("Income Tax =", tax)




# 19. Check if a student passes (minimum 35 marks in each subject).

# math=int(input("Enter math marks"))
# science=int(input("Enter science marks"))
# marathi=int(input("Enter marathi marks"))

# if math >=35 and science >=35 and marathi >=35:
#     print("pass")
# else:
#     print("fail")


# 20. Find whether a number is within a given range.

# num=int(input("Enter a number:"))
# lower=int(input("Enter lower limit:"))
# upper=int(input("Enter upper limit:"))

# if lower<=num <=upper:
#    print("number is within the range")
# else:
#    print("number is outside the range")



# 21. Build a simple calculator using if-elif-else (+, -, *, /).

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operator=input("Enter operator(+,-,*,/):")

if operator =="+":
    print("Result=",num1+num2)
elif operator =="-":
    print("Result=",num1-num2)
elif operator == "*":
    print("Result=",num1*num2)
elif operator =="/":
    print("Result=",num1/num2)
else:
    print("invalid value")
                

# 22. Check if a year is a century leap year.

# num=int(input("Enter a yearaa:"))
# if num % 4==0:
#     print("this is leap year")
# else:
#     print("this is not leap year")
     

# 23. Determine the season based on the month number.


# month = int(input("Enter month number: "))

# if month == 3 or month == 4 or month == 5:
#     print("Spring")
# elif month == 6 or month == 7 or month == 8:
#     print("Summer")
# elif month == 9 or month == 10 or month == 11:
#     print("Autumn")
# elif month == 12 or month == 1 or month == 2:
#     print("Winter")
# else:
#     print("Invalid month")



# 24. Find the number of days in a month.

# month = int(input("Enter month number: "))

# if month == 2:
#     print("28 or 29 days")
# elif month in [4, 6, 9, 11]:
#     print("30 days")
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 days")
# else:
#     print("Invalid month")


# 25. Check whether a password meets minimum conditions (length, digits, etc.).

# password = input("Enter password: ")

# if len(password) >= 8 and any(char.isdigit() for char in password):
#     print("Password is valid")
# else:
#     print("Password is invalid")


# 26. Determine ticket price based on age category.


# age = int(input("Enter your age: "))

# if age < 5:
#     print("Ticket is free")
# elif age <= 12:
#     print("Ticket price = ₹50")
# elif age <= 60:
#     print("Ticket price = ₹100")
# else:
#     print("Ticket price = ₹70")


# 27. Calculate discount based on purchase amount.

# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = 20
# elif amount >= 3000:
#     discount = 15
# elif amount >= 1000:
#     discount = 10
# else:
#     discount = 0

# discount_amount = amount * discount / 100
# final_amount = amount - discount_amount

# print("Discount =", discount, "%")
# print("Discount amount =", discount_amount)
# print("Final amount =", final_amount)



# 28. Check if a person is eligible for a driving license (age and eyesight condition).

# age = int(input("Enter your age: "))
# eyesight = input("Do you have normal eyesight? (yes/no): ")

# if age >= 18 and eyesight == "yes":
#     print("Eligible for driving licence")
# else:
#     print("Not eligible for driving licence")


# 29. Create a login system with username and password validation.

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "shivani" and password == "12345":
#     print("Login successful")
# else:
#     print("Invalid username or password")


# 30. Create a menu-driven program using if-elif-else with options like:
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice: "))

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     if b != 0:
#         print("Result =", a / b)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid choice"


