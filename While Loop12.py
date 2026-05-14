# Basic While Loop

# i = 1
# while i<=5:
#     print(i)
#     i +=1
# i = 1
# while i<=10:
#     print(i)
#     i +=1

# Countdown
# i = 10
# while i>0:
#     print(i)
#     i-=1

# Basic While Loop
# i = "I love you Komal"
# while i == "I love you Komal":
#     print(i)

# Ask user until valid Input
# num =" "
# while not num.isnumeric():
#     num=input("Enter any number :")
#     print("Enter only number")
# print("Number accepted :",num)

# Basic While Loop

# Increment
# i = 1
# while i<=5:
#     print(i)
#     i+=1

# Decrement
# i=5
# while i>0:
#     print(i)
#     i-=1

# Square
# i=1
# while i<=10:
#     print(i*i)
#     i+=1

# Countdown
# i = 10
# while i>0:
#     print(i)
#     i-=1

# # Ask User enter valid Input
# num = " "
# while not num.isnumeric():
#     num = input("Enter number :")
#     print("Enter only number")
# print("Number Accepted",num)

# Loop through list using While
# items = ["Apple","Banana","Grapes","Orange","Papaya"]
# i=0
# while i < len(items):
#     print(items[i])
#     i +=1

# Using Break
# i = 1
# while i<=10:
#     if i == 5:
#         break
#     print(i)
#     i +=1

# i = 1
# while i<=10:
#     print(i)
#     if i == 5:
#         break
#     i +=1

# Using Continue
# i = 0
# while i<10:
#     i+=1
#     if i % 2 == 0:
#         continue
#     print(i)

# Using Password
# password = " "
# attempts = 0
# while password != "admin123" and attempts < 3:
#     password = input("Enter your password :")
#     attempts +=1
#     if password == "admin123":
#         print("Login Successfully")
#     else:
#         print("Wrong Password and you have only 3 attempts",attempts)
#         if attempts == 3:
#             print("Attempts Expired")

# Using Password
# password = " "
# attempts = 0
# while password != "Komal" and attempts<2:
#     password = input("Enter password :")
#     attempts +=1
#     if password == "Komal":
#         print("Login Successfully")
#     else:
#         print("Wrong password and you have only 2 attempts",attempts)
#         if attempts == 2:
#             print("Attempts Expired")

# Assignment
# print numbers from 10 to 1
# i=10
# while i>0:
#     print(i)
#     i-=1

# Ask user their favorite colour until they enter something
# color = " "
# while color.strip() == " ":
#     color = input("Enter your favourite color :")
#     if color.strip() == "":
#         print("Please Enter something")

# print("Your favorite color is :",color)

color = ""
while color.strip() == "":
    color = input("Enter your favorite color: ")
    if color.strip() == "":
        print("Please enter something!")

print("Your favorite color is:", color)











