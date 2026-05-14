# Lists
fruits = ["Apple","Mango","Banana"]
# print(fruits[0])
# print(fruits[-1])
# print(fruits)

# # Update List
# fruits[1]="Orange"
# print(fruits)

# # Add Items
# fruits.append("Grapes")
# print(fruits)

# fruits.insert(1,"Kiwi")
# print(fruits)

# # Remove Items
# fruits.remove("Grapes")
# print(fruits)

# fruits.pop(2)
# print(fruits)

# # Slicing
# value = [10,20,30,40,50,60]
# print(value)
# print(value[:3])
# print(value[-2:])

# # # Looping
# for f in fruits:
#     print("Fruit",f)
#     print(f)

# # Clean city names
# raw = ["  mUMBai ","DeLhI","pune  "]
# clean=[ ]
# for c in raw:
#     clean.append(c.strip().title())
# print(clean)

# # Replace names
# city = ["Bengluru","kulown","Kapur"]
# cities = [ ]
# for ci in city:
#     cities.append(ci.replace("Bengluru","Bengaluru")
#                   .replace("kulown","Lucknow")
#                   .replace("Kapur","Kanpur"))
# print(cities)

# # Extract Years
# codes = ["Laptop-2024","Phone-2023"]
# years = [ ]
# for c in codes:
#     years.append(c[-4:])
# print(years)

# Assignment
# Create a list of 5 fruits and print each using a loop.
fruits = ["Apple","Mango","Banana","Grapes","Papaya"]
for f in fruits:
    print(f)
# Replace any one item in the list
fruits[3] = "Watermelon"
print(fruits)

# Clean a list of messy country names:
# countries = [" inDIA ", " usa", "jAPAn "]
# country = [ ]
# for c in countries:
#     country.append(c.strip().title())
# print(country)

# Remove wrong names and correct spelling.
countries = [" inDIA ", " usa", "jAPAn "]
country = [ ]
for c in countries:
    country.append(c.replace("inDIA","India").replace("usa","Usa").replace("jAPAn","Japan"))
print(country)

# Extract last 4 digits from employee codes:
codes = ["EMP-9001", "EMP-8765", "EMP-7777"]
for c in codes:
    print(c[-4:])




