"""
Week 1
"""

# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.

# for i in range(1,11):
#     print(i)

"""---------------------------------------------------"""
# Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

# user_number = int(input("Please enter a number: "))
# for i in range(1,user_number+1):
#     if i % 2 == 0 :
#         print(i)
# counter = 1
#
# while counter <= user_number:
#     if counter % 2 == 0:
#         print(counter)
#     counter +=1

"""---------------------------------------------------"""
# Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values (including the end value) on the screen.

# start_value = int(input("Please enter a starting value: "))
# end_value = int(input("Please enter a ending value: "))
#
# for i in range(start_value,end_value+1):
#     print(i)

"""---------------------------------------------------"""
# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

# nummer = int(input("Please enter a number: "))
# if nummer % 2 == 0:
#     print("The number you enter is an even number.")
# else:
#     print("This number you entry is an odd number.")

"""---------------------------------------------------"""
# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial.
#             Factorial is the product of all positive integers between a number itself and 1.
#             For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120

# factorial_user_input = int(input("Please enter the number to calculate the factorial: "))
# while factorial_user_input <= 0:
#     factorial_user_input = int(input("You have entered an incorrect entry! Please re-enter the number to calculate the factorial: "))
# factorial_result = 1
# #Calculating factorial
# for i in range(1,factorial_user_input+1):
#     factorial_result *= i
# print("Factorial:",factorial_result)

"""---------------------------------------------------"""
# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.
# user_number = int(input("Please enter a number: "))
# prime_control = True
# if user_number >= 3 :
#     for i in range(3,int(user_number ** 0.5)):
#         if user_number % i == 0:
#             prime_control = False
#             break
# if prime_control :
#     print(f"The number you entered, {user_number}, is a prime number.")
# else:
#     print(f"The number you entered, {user_number}, is not a prime number.")

"""---------------------------------------------------"""
# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?
#
# list_fibonacci =[1,1]
# index_fibonacci = 2
# digit_number = 0
# while len(str(digit_number))!= 100:
#     list_fibonacci.append(list_fibonacci[index_fibonacci-2]+list_fibonacci[index_fibonacci-1])
#     digit_number = list_fibonacci[index_fibonacci-2]+list_fibonacci[index_fibonacci-1]
#     index_fibonacci += 1
# # print(list_fibonacci)
# print(index_fibonacci)
# print(digit_number)

"""---------------------------------------------------"""
# # Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

# user_string = input("Please enter a word: ")
# # Variable to create the reverse of the string
# reserve_string = ""
# for i in user_string:
#     reserve_string = i + reserve_string
# print(reserve_string)

"""---------------------------------------------------"""
# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

# paindrome_str = input("Please enter a word: ")
# paindrome_control = True
# for i in range(int(len(paindrome_str)/2)):
#     if (paindrome_str[i] != paindrome_str[-1-i]) :
#         paindrome_control= False
#         break
# if paindrome_control :
# # if paindrome_str == paindrome_str[::-1]:
#     print("The word you entered is a paindrome.")
# else:
#     print("The word you entered is a not paindrome.")

"""---------------------------------------------------"""
# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value.
# (You can look on the internet for the weight index calculation)
# To do this, ask the user for their weight and height measurements.
# weight index If it is below 25, it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.

# user_weight = int(input("Please enter your weight: "))
# user_height = float(input("Please enter your height(cm): "))/100
# user_weight_index = user_weight / (user_height ** 2)
# if user_weight_index <25 :
#     print("You are weak")
# elif (user_weight_index >= 25)  and (user_weight_index <= 30) :
#     print("You are normal")
# elif (user_weight_index > 30) and (user_weight_index < 40) :
#     print("You are overweight")
# else:
#     print("You have danger of obesity!!!")
# print(user_weight_index)

"""---------------------------------------------------"""
# Question 11: How to write a Python program that finds the largest of three numbers entered by a user?

# user_number1,user_number2,user_number3 = int(input("Please enter first number: ")), int(input("Please enter second number: ")),int(input("Please enter third number: "))
# largest_number = user_number1
# if largest_number < user_number2:
#     largest_number =user_number2
# if largest_number < user_number3:
#     largest_number = user_number3
# print("The largest number you enter:",largest_number)

"""---------------------------------------------------"""
# # Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average.
# # If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen.
# # This printing process is 4 lessons. and the lessons will be written one after the other.

# List where courses information will be kept
# courses = list()
# for i in range(4):
#     course ={}
#     course["id"] = i+1
#     course["name"] = input("Please enter course name: ")
#     course["midterm"]= int(input("Please enter midterm exame grade: "))
#     course["final"] = int(input("Please enter final exame grade: "))
#     course["average"] = ((course["midterm"] * 0.4) + (course["final"] * 0.6))
#     if course["average"] < 50:
#         course["result"]="FAILED"
#     else:
#         course["result"] = "SUCCESSFUL"
#     courses.append(course)

# for i in courses:
#     print(f"Student in {i["name"]} course: ",i["result"],"  Avarage:",i["average"])

# print(courses)

print(int(1.1))
print(int(1.6))
print(int(1.9))