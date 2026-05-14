# Day 11 For Loop :
# word = "Python"
# for i in word:
#     print(word)

# word = "Python"
# for i in word:
#     print(i)

# word = "Python"     # If I need Python word 5 times then we use range.
# for i in range(1,6):
#     print(word)

# # Total Calculation
# marks = [1,3,6,8]
# total = 0
# for m in marks:
#     total +=m
# print("Total :",total)

# Print all numbers from 1 to 10
# for i in range(1,11):
#     print(i)

# Print even numbers from 1 to 20
# for num in range(1,21):
#     if num % 2 == 0:
#         print(num)

# Print odd number from 1 to 15
# for num in range(1,16):
#     if num % 2 != 0:
#         print(num)

# Clean City Names
# city = [" MUmbAi  ", "    PunE"]
# cities = [ ]
# for c in city:
#     cities.append(c.strip().title())
# print(cities)

# # Loops with if Condition
# nums = [2,18,1,4,12,19]
# for n in nums:
#     if n % 2 == 0:
#         print(n,"Even Number")
#     else:
#         print(n,"Odd Number")

# Print even number and odd number
# values = range(1,21)
# for i in values:
#     if i % 2 == 0:
#         print(i,"Even Number")
#     else:
#         print(i,"Odd Number")

# Fixing Spelling Mistakes
# wrong_list = ["Bengluru","LknOW","kAnPuER"]
# spell = [ ]
# for w in wrong_list:
#     spell.append(w.replace("Bengluru","Bengaluru").replace("LknOW","Lucknow").replace("kAnPuER","Kanpur"))
# print(spell)

# # Looping with dictionary
# student = {"name":"Komal","age": 25,"City":"Lucknow"}
# for key,value in student.items():
#     print(key,"=",value)

# # Find the sum of all numbers in list
# num = [2,4,6,8]
# values = 0
# for i in num:
#     values += i
# print(values)

# # # Count how many items are in a list without using len()
# num = [2,4,6,8]
# count = 0
# for i in num:
#     count +=1
# print("Count",count)

# # Print each chararcter of string
# text = "Python"
# for i in text:
#     print(i)

# Count vowels
# vowels = ["a","e","i","o","u"]
# count = 0
# for v in vowels:
#     count += 1
# print("count",count)

# Count vowels in a string
# text = "String"
# count = 0
# for t in text:
#     if t.lower() in "aeiou":
#         count+=1
    
# print(count)

# # Count how many items are in a list using len()
# num = [2,4,6,8]
# count = len(num)
# print(count)

# # Find the largest number in a string
# marks = [45,78,23,90,67]
# print(max(marks))
# print(min(marks))

# Print multiplication table of 5 using for loop
# for i in range(1,11):
#     print(i*5)

# Reverse a string using loop
# text = "Hello"
# print(text[::-1])

# Python Whie Loop
# i = 1
# while i<=5:
#     print(i)
#     i+=1

# i = 10
# while i>=1:
#     print(i)
#     i-=1

# i = 1
# while i <=10:
#     print(i*i)
#     i +=1

# items = ["Apple","Banana","Orange","Kiwi"]
# i = 0
# while i<len(items):
#     print(items[i])
#     i+=1

# vege = ["Tomato","Potato","Brinjal","Gourd"]
# a = 0
# while a<len(vege):
#     print(vege[a])
#     a+=1

# Break
# i = 1
# while i<=10:
#     if i == 5:
#         break
#     print(i)
#     i+=1

# Using Continue
# i = 0
# while i<=10:
#     i+=1
#     if i%2==1:
#         continue
#     print(i)

# Using password
# Password = " "
# attempts = 0

# while Password != "Komal" and attempts < 2:
#     Password = input("Enter your pssword :")
#     attempts+=1
# if Password == "Komal":
#     print("Login Successfully")
# else:
#     print("Wrong Password",attempts)
#     if attempts == 2:
#         print("Attempts Expired")

# Password = ""
# attempts = 0

# while Password != "Komal" and attempts < 2:
#     Password = input("Enter your Password: ")
#     attempts += 1

# if Password == "Komal":
#     print("Login Successfully")
# else:
#     print("Wrong Password")
    
#     if attempts == 2:
#         print("Attempts Expired")


# Lists in python
# fruits = ["Apple","Banana","Kiwi","Orange"]
# print(fruits[0])
# print(len(fruits))
# print(fruits[3])

# # Update List
# fruits[0] = "Grapes"
# print(fruits)

# # Add items
# # Append
# fruits.append("Papaya")
# print(fruits)

# # Insert
# fruits.insert(1,"Watermelon")
# print(fruits)

# # Remove
# fruits.remove("Banana")
# print(fruits)

# # Pop
# fruits.pop(0)
# print(fruits)

# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# Slicing
value = [10,20,30,40]
print(value[1:4])
print(value[::-1])

# Looping
# Foor Loop
# fruits = ["Apple","Banana","Kiwi","Orange"]
# for f in fruits:
#     print(f)

# # While Loop
# fruits = ["Apple","Banana","Kiwi","Orange"]
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# Correct City names
# city = ["MuMBai  ","   pUnE "," DeLhI  "]
# cities = [ ]
# for c in city:
#     cities.append(c.strip().title())
# print(cities)

# Replace
# place = ["Lknocw ","kANpUr"]
# places = [ ]
# for p in place:
#     places.append(p.replace("Lknocw","Lucknow").replace("kANpUr","Kanpur").strip().title())
# print(places)

# # Extract Year
# codes = ["Laptop-2011","Laptop-2015"]
# code = [ ]
# for c in codes:
#     code.append(c[-4:])
# print(code)

# Tuple
# a = (1,2)
# b = (3,4)
# print(a+b)

# Packing and Unpacking
# data = ("Laptop",45000,"Black")
# product,price,Color = data
# print(f"Product:{product},Price:{price},Color:{Color}")
# print(data)
    
# # Nested tuple inside List
# employees = [("E101","Abhishek","Lucknow"),
#              ("E102","Komal","Kanpur")]
# for Eid,Name,Location in employees:
#     # print(f"Eid : {Eid}, Name : {Name}, Location : {Location}")
#     print(Eid,Name,Location)

# Dictionaries
student = {"Name": "Abhishek",
           "Age": "25",
           "Location" : "Lucknow"}
# print(student)
# print(student["Name"])
# print(student["Age"])
# print(student["Location"])

# # Adding and Updating
# student["Marks"] = "85"
# print(student)
# student["Location"] = "Kanpur"
# student["Name"] = "Komal"
# print(student)

# # Removing
# student.pop("Marks")
# print(student)

# Dictionary Method
print(student.keys())
print(student.values())
print(student.items())
print(student.get("Name"))

# Looping
# for k in student:
#     print(k,student[k])

# Nested Dictionary
employees = {
    "E101" : {"name":"Komal","age" : 28},
    "E102" : {"name":"Abhishek","age":20}
}
print(employees["E101"])
print(employees["E102"]["age"])

# Mapper
mapper = {
    "mombai" : "Mumbai",
    "Kolkatta" : "Kolkata"
}
print(mapper["mombai"])











    
