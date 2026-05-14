# # # Sets
# # # Create Sets
# # fruits = {"Apple","Banana","Orange"}
# # print(fruits)

# # # Add Items
# # fruits.add("Grapes")
# # print(fruits)

# # # Remove Items
# # fruits.discard("Apple")
# # print(fruits)

# # # Set Operation
# # # Union (a|b)
# # a = {1,2,3}
# # b = {3,4,5}
# # print("Union :",a|b)

# # # Intersection (a & b) It is used to print common Output
# # print("Intersection :",a & b)

# # # Difference (-) It is only print ("a") part and not to print common part.
# # print("Difference :",a-b)

# # # Symmetric Difference (^) It is not print common number it will print all number accept common number.
# # print("Symmetric Difference :",a ^ b)

# # # Remove Duplicates {By the help of ("SET") can remove the duplicates in Sets}
# # cities = {"Mumbai","Australia","Thailand"}
# # print(set(cities))

# # # Missing Values
# # list1 = {"SQL","Python","Power BI","Excel"}
# # list2 = {"SQL","Power BI"}
# # print(list1-list2)

# # # Symmetric Difference Skill
# # deptA = {"Excel","SQL","Python"}
# # deptB = {"Excel","Python","Power BI"}
# # print("Symmetric Difference :",deptA ^ deptB)

# # #---------------------------------------------------------------------------------------------------

# # # Range and Loops in Python
# # # print 1 to 5 number
# # for i in range(1,6):
# #     print(i)

# # # Print for even number
# # for i in range(1,11):
# #     if i % 2 == 0:
# #         print("Even Number",i)
# #     else:
# #         print("Odd Number",i)

# # # Print for even number
# # for i in range(0,20,2):
# #     print(i)

# # for i in range(1,20,2):
# #     print("Odd Number",i)

# # # Countdown from 10 to 1
# # for i in range(10,0,-1):
# #     print(i)

# # for i in range(10,1,-1):
# #     print(i)

# # # Loop through list using Index
# # items = ["Pen","Book","Pencil"]
# # for i in range(len(items)):
# #     print(i,items[i])

# # print(items[1:3])

# # # Generate Employee ID
# # for i in range(1,11):
# #     print("EMP - ",i)

# # # Create Year List
# # years = [ ]
# # for i in range(2015,2026):
# #     years.append(i)
# # print(years)

# # # Clean Cities Name
# # # cities = ["mUMbAi  ","   PUnE"]
# # # for c in range(len(cities)):
# # #     cities[c] = [cities[c].strip().title()]
# # # print(cities)
# # cities = ["mUMbAi  ","   PUnE"]
# # value = [ ]
# # for c in cities:
# #     value.append(c.strip().title())
# # print(value)

# # # Extract Last Four digit
# # ids = ["EMP-001122","EMP-550044"]
# # for i in range(len(ids)):
# #     print(ids[i][-4:])

# # # Nested Loop in range
# # for i in range(1,11):
# #     for j in range(1,3):
# #         print(f"i : {i},j : {j}")

# # # Functions in Python
# # Without argument
# # def greet():
# #     print("Hello Abhishek Singh")
# # greet()

# # # With Argument
# # def name(name):
# #     print("My name is",name)
# # name("Komal")

# # def Welcome(age):
# #     print("My age is ",age)
# # Welcome(28)

# # def add(a,b):
# #     print("Addition",a+b)
# # add(1,5)

# # def Sub(c,d):
# #     print("Subtraction",c-d)
# # Sub(4,2)

# # # Return
# # def add(a,b):
# #     return a+b
# # Total = add(1,3)
# # print(Total)

# # def multiple(x):
# #     return(x*2)
# # Total = multiple(Total)
# # print(Total)

# # # Clean text
# # def text(letter):
# #     return letter.strip().title()
# # result = text("   MUmbAi ")
# # print(result)

# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai","mumbai")
#     city = city.replace("kolkatta", "kolkata")
#     return city.title()
# print(fix_city("momBai"))
# print(fix_city("kolkatta"))

# # def fix_city(city):
# #     city = city.lower().strip()
# #     city = city.replace("mombai", "mumbai")
# #     city = city.replace("kolkatta", "kolkata")
# #     return city.title()

# # print(fix_city("momBai"))
# # print(fix_city("kolkatta"))

# # Get Code
# def get_year(code):
#     return code[-4:]
# print(get_year("Laptop-2024"))

# # Get to know perfect email
# def is_valid_email(email):
#     return "@" in email and "." in email
# print(is_valid_email("Abhi@gmail.com"))

# # Total Salary
# def total_salary(basic,bonus):
#     return basic+bonus
# print(total_salary(200,500))

# # Number
# def stats(num):
#     return min(num),max(num),sum(num)
# print(stats([10,20,30,50]))

# # Clean list values
# def clean_list(values):
#     cleaned = [ ]
#     for v in values:
#         cleaned.append(v.strip().title())
#         return cleaned
# print(clean_list(["mUmbai  ","pUnE "]))

# # String, List and Number Function
# # String Function
# text = "Banana"
# print(text.count("a"))

# print("Hello.py".endswith (".py"))
# print("sales_force" .startswith ("sales"))

# print("123".isdigit())
# print("ABC".isalpha())

# print("ABC12".isalnum())

# print("Line1\n,Line2\n,Line\n".splitlines())

# lines = "Line1\nLine2\nLine3".splitlines()
# for line in lines:
#      print(line)

# # List Functions
# # Sort
# nums = [5,3,7,2]
# nums.sort()
# print(nums)

# values = [10,40,90,20]
# print(max(values),min(values),sum(values))

# mylist = [1,3,1,2,5,4,7,9]
# print(mylist.count(1))
# print(mylist.index(2))
# print(mylist.index(9))

# # Extend
# a = [1,2]
# c = [3,4]
# a.extend(c)
# print(a)

# # Number Functions
# print(round(3.456,2))

# print(abs(-50))

# print(pow(10,2))

# print(divmod(10,3))

# print(sum([5,5,5],5))

# # Practical Example

# products = [" MoUsE ","  LapToP"]
# clean = [p.strip().title() for p in products]
# clean.sort()
# print(clean)

# email = ["Abhi@gmail.com","Komal@gmail.com"]
# mail = [mail[mail.find("@")+1:] for mail in email]
# print(mail)

# mobiles = ["9621622169","9695069511","1234"]
# valid = [m for m in mobiles if m.isdigit() and len(m) == 10]
# print(valid)

# File Handling
# Reading Full File
# with open("text.txt","r") as f:
#      print(f.read())

# with open("text.txt","r") as f:
#      for i in f:
#           print(i.strip().title())

# with open("text.txt","r") as f:
#      print(f.read().strip().title())

# # Writing
# with open("Data.txt","w") as f:
#      f.write("Day-20 File Handling\n")
#      f.write("Day-20 Learning and Reading\n")

# # Appending
# with open("Data.txt","a") as f:
#      f.write("Appending Line 2\n")
#      f.write("Appending full course\n")

# Cleaning data in file
cleaned = [ ]
with open("text.txt","r") as f:
     for line in f:
          cleaned.append(line.strip().title())
with open("cleaned.txt","w") as f:
     for city in cleaned:
          f.write(city + "\n")

# Clening data file
cities = [ ]
with open("text.txt","r") as f:
     for i in f:
          cities.append(i.strip().title())
with open("cities.txt","w") as f:
     for c in cities:
          f.write(c + "\n")

# Counting lines
count = 0
with open("text.txt","r") as f:
     for _ in f:
          count+=1
     print("Total lines",count)


   




