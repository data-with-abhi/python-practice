# INDEXING
# name = "Komal"
# print(name)
# print(name[0])
# print(name[4])

# SLICING
Product="Laptop pro 2024"
print(Product[0:6])
print(Product[-4:])
print(Product[-8:])

text = "DATAANALYSIS"
# Extracting first four data
print("First four letter is ", text[0:4])
print("All letters ",text[4:12])
print("Backward letter",text[-12:])
print("Alternate letter",text[0:12:2]) #Skip text

# Reverse String
print("Reverse String :",text[::-1])
print("Reverse String :",text[-8:][::-1])
print("Reverse String :",Product[7:10][::-1])
print("Reverse String :",Product[0:6][::-1])
print("Reverse String :",Product[11:15][::-1])
print("Reverse String :",text[4:12][::-1])

# Extracting first name using Slicing
full_name = "Rohit Sharma"
print("First Name :",full_name[:5])
print("Last Name :",full_name[6:12])
print("Last Name :",full_name[-6:])
