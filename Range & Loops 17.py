# Range and Loops
# Print 1 to 5 number
# for i in range(1,6):
#     print(i)

# for i in range(6):
#     print(i)

# Print for even numbers
# for i in range(0,20,2):
#     print(i)

# # Print Odd Number
# for i in range(1,20,2):
#     print(i)

# Countdown from 10 to 1
# for i in range(10,0,-1):
#     print(i)

# Loop through list using Index
items = ["Pen","Book","Laptop"]
for i in range(len(items)):
    print(i,items[i])

# Generate Employees Id.
for i in range(1,6):
    print("EMP-",i)

# Create Years List
years = [ ]
for i in range(2015,2026):
    years.append(i)
print(years)

# Create Month list
month = [ ]
for m in range(1,13):
    month.append(m)
print(month)

# Clean cities names
cities = ["  mUMBAi ","PUnE  ","  KAnPuR"]
for c in range(len(cities)):
    cities[c]=cities[c].strip().title()
print(cities)

# Extract Lat 4 digit number
ids = ["EMP-001122","EMP-550044","EMP-990011"]
for i in range(len(ids)):
    print(ids[i][-4:])


for i in range(1,11):
    for j in range(1,3):
        print(f"I value : {i},J Value : {j} ")