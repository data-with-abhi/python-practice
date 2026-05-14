# Dictionary
student = {"name":"Komal","age":25,"city":"Pune"}
# print(student)

# print(student["name"])
# print(student["age"])
# print(student["city"])

# # Adding and Updating
# student["age"] = 28
# student["city"] = "Kanpur"
# student["marks"] = 85
# print(student)

# # Removing
# student.pop("age")
# print(student)

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

# Looping
for k in student:
    print(k,student[k])

# Nested Dictionary
employees = {
    "E101" : {"name":"Komal","marks":85,"city":"Kanpur"},
    "E102" : {"name":"Abhishek","marks":90,"city":"Knpur"}
}
print(employees["E101"]["name"])
print(employees["E102"]["marks"])

# Mapping wrong - correct
mapper = {
    "mombai" : "Mumbai",
    "Kolkatta" : "Kolkata"
}
print(mapper["mombai"])
print(mapper["Kolkatta"])

# Dictionary for Counting Frequency (Real DA Work)
words = ["apple","apple","banana","mango","banana"]
freq={}
for w in words:
    if w in freq:
        freq[w]+= 1
    else:
        freq[w]=1
print(freq)



