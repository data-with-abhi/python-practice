import csv

# Read entire CSV
with open("Ch-9.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# # Dict Reader
# with open("ch-9.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["Name"],row["City"])

# Calculation
total = 0
with open("ch-9.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total +=int(row["Age"])*int(row["Marks"])
print("Calculation",total)

# Filter by city
Gurgaon = [ ]
with open("ch-9.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["City"]=="Gurgaon":
            Gurgaon.append(row)
print(Gurgaon)

# Filter by Age
Age = [ ]
with open("ch-9.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Age"] == "21":
            Age.append(row)
print(Age)

