# Create Sets
fruits = {"Apple","Mango","Apple","Banana"}
print(fruits)

# Add Items
fruits.add("Orange")
print(fruits)

# Remove Items
fruits.discard("Banana")
print(fruits)

# Set Operations
a = {1,2,3}
b = {3,4,5}
print("Union",a|b)
print("Intersection",a & b)
print("Difference",a-b)
print("Difference",b-a)
print("Symmetric Difference",a^b)

# Remove Duplicate
cities = ["Mumbai","Pune","Delhi","Mumbai"]
unique = set(cities)
print("Unique cities :",unique)

# city = {"Mumbai","Pune","Delhi","Mumbai"}
# print(city)

# city = ("Mumbai","Pune","Delhi","Mumbai")
# u = set(city)
# print("U City",u)

# Missing Values
list1 = {"SQL","Excel","Power BI"}
list2 = {"SQL","Power BI"}
missing = list1-list2
print("Missing Values",missing)

# Symmetric Difference Skills
deptA = {"SQL","Excel","Python"}
deptB = {"Excel","Python","Power BI"}
Symmetric = deptA ^ deptB
print("Common",Symmetric)
