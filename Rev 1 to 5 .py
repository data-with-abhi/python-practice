# Print Function
# print("Hello World")
# print("My name is Komal Singh")

# Variables and Comments
# name = "Komal Singh"
# print("Hello ",name)
# print("Your most welcome to join our team ",name)
# age = 25
# print("My age is",age)
# take the output by the help of variable.

## Data Types
# 1.1 Text Data Type
# name = "Komal Singh"
# print("My name is",name)
# print(type(name))

# # 2. Numeric Data Type
# # 2.2 Integer
# num = 24
# print("My number is: ",num)
# print(type(num))

# # 2.3 Float
# quantity = 28.1 # here we mention the type of this quantity.
# print("My order quantity is",quantity)
# print("My quantity data type is",type(quantity))

# # 2.4 Complex Number
# num1 = 2+5j
# print("My complex number is",num1)
# print(type(num1))

# # 3. Boolean Data Type
# is_paid = True
# print(is_paid)
# print(type(is_paid))

# # 4. Sequence Data Type
# # 4.1 List
# city = ["Mumbai","Delhi","Lucknow","Kanpur"]
# print(city)
# print(type(city))

# # 4.2 Tuple
# country = ("India","America","France","Switzerland")
# print(country)
# print(type(country))

# # 4.3 Range
# num = range(5)
# print(list(num))
# print(type(num))

# 5. Mapping Type
# Dictionary
# student = {
#     "name" : "Komal Singh",
#     "age" : "27",
#     "City" : "Kanpur"
# }
# print(student)
# print(type(student))

# # 6. Set Data Type
# num1 = {1,2,2,3,4,5,7,7,}
# print(num1)
# print(type(num1))

# # 7. None Type # It means no value
# Value = None 
# print(Value)
# print(type(Value))

## OPERATORS
# Airthmetic Operator
# num1 = 5
# num2 = 2
# print(num1-num2)
# print("Multiplication of this number is ",num1*num2)

# # Assignment Operator
# value = 50
# print(value)
# value += 10
# print(value)
# value -= 20
# print(value)

# # Comparison Operator
# x1 = 5
# x2 = 15
# x3 =25
# x4 = 35
# print(x1>x2)
# print(x3==x3)
# print(x1<x2)

# Logical Operator
# p1 = 6
# p2 = 12
# p3 = 18
# p4 = 24
# print(p1<p2 and p4>p3)
# print(p1<p2 or p4<p3)
# print(not(p1<p2))

# # Identity Operator
# a1 = 2
# a2 = 3
# a4 = 4
# print(a1 is a2)
# print(a1 is not a2)

# # Membership Operator
# print("'a' in mango",'a' in 'mango')
# print("'a' not in mango",'a' not in 'mango')

## Input, Typecasting and Basic Calculation
# name = input("what is your name ")
# print(name)
# print(type(name))

# value =int(input("What is your age "))
# print(value)
# print(type(value))

# Convert Number to string
# sales = 50000
# name = "Total Sales " + str(sales)
# print(name)

# Total Sales Calculator
# product = input("Product Name : ")
# Quantity = int(input("Enter quantity : "))
# price_per_unit = float(input("Enter the price : "))

# Total_sales_price = Quantity * price_per_unit
# print("Product :",product)
# print("Total_sales_price :",Total_sales_price)

# print("Mouse  is",Total_sales_price,"and it is very costly")

# Assignment : Salary Slip Calculator
Employee_Name = input("Employee Name : ")
Basic_Salary = int(input("Basic Salary : "))
Bonus_Amount = int(input("Bonus Amount : "))
Tax_Percentge = int(input("Tax Percentage : "))

Gross_Salary = Basic_Salary + Bonus_Amount
Tax_Amount =( Gross_Salary * Tax_Percentge )/100
Net_Salary = Gross_Salary - Tax_Amount

print("Gross Salary is ",Gross_Salary)
print("Tax Amount is ",Tax_Amount)
print("Net Salary is ",Net_Salary)

print("Employee name is ",Employee_Name,"her gross salary is ",Gross_Salary,"and the salary is quiet good")























