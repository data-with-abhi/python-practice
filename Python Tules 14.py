# Create Tuple
fruits = ("Apple","Banana","Mango")
print(fruits)

#Indexing
print(fruits[0])
print(fruits[-1])

#Slicing
nums = (10,20,30,40,50)
print(nums[1:4])

#Looping
colors = ("Red","Green","Blue")
for c in colors:
    print(c)

# Tuple Length
length = len(colors)
print(length)

# Concatenation
a = (1,2)
b = (3,4)
print(a+b)

# Pcking and Unpacking
data = ("Laptop",45000,"Black")
product,price,color = data
print(product,price,color)
print(f"Product : {product}, Price : {price}, Color : {color}")

# Nested Tuple inside List
employees = [("E101","Rohit","Pune"),("E102","Sneha","Mumbai")]
for Eid,Name,City in employees:
    print(Eid,Name,City)