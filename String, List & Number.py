# # String Functions
# text = "Banana"
# print(text.count("a"))

# print("Hello.py".endswith(".py"))
# print("Sales_product".startswith("Sales"))

# print("123".isdigit())
# print("ABC".isalpha())
# print("ABc12d".isalnum())

# print("Line1\nLine2\nLine3")
# print("Line1\nLine2\nLine3".splitlines())

# # # List Functions
# nums = [5,3,4,7,2]
# nums.sort()
# print(nums)

# fruits = ["Banana","Grapes","Apple"]
# fruits.sort()
# print(fruits)

# marks = [10,20,50,30]
# print(min(marks),max(marks),sum(marks))

mylist = [1,2,4,1,3,6]
print(mylist.index(2))
print(mylist.index(6))
print(mylist.count(1))

a = [1,2]
b = [3,4]
a.extend(b)
print(a)

# Number Functions
# Round
print(round(3.678,2))

#Absolute
print(abs(-50))

# Power
print(pow(10,3))

# Division Mode (divmod)
print(divmod(10,3))

# Practical Example
products = ["  LapTOp ","mOuSe"]
clean = [p.strip().title() for p in products]
clean.sort()
print(clean)

emails = ["Abhi@gmail.com","Komal@yahoo.com"]
domains = [mail[mail.find ("@")+1:] for mail in emails]
print(domains)

mobiles = ["9621622169","9695069511","12345"]
valid = [m for m in mobiles if m.isdigit() and len(m)==10]
print(valid)