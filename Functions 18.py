# FUNCTIONS (def,return)
# def greet():
#     print("Hello Python Learners")
# greet()

# def welcome(name):
#     print("Welcome ",name)
# welcome("Komal")

# def love(name):
#     print("I love You",name)
# love("Komal")

# def add(a,b):
#     print("Total :",a+b)
#     print("Multiply :",a*b)
# add(1,3)

# def sub(c,d):
#     print("Subtract :",c-d)
# sub(5,1)

# Return
# def add(a,b):
#     return a + b

# def multiple(x):
#     return x*2

# result = multiple(add(1,3))
# print(result)

# Clean Text Value
# def value(text):
#     return text.strip().title()

# result = value("  mUmBaI  ")
# print(result)

# For Multiple Condition
# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai","mumbai")
#     city = city.replace("kolkatta","kolkata")
#     return city.title()

# print(fix_city("mombai"))
# print(fix_city("kolkatta"))

# Get code
def get_year(code):
    return code[-4:]
print(get_year("Laptop-2024"))

# Find Perfect email
# def is_valid_email(email):
#     return "@" in email and "." in email
# print(is_valid_email("singhshekabhi099@gmail.com"))

# def total_salary(salary,bonus):
#     return salary + bonus
# print(total_salary(2000,3000))

# def stats(num):
#     return min(num),max(num),sum(num)/len(num)
# print(stats([10,20,30]))

# # Clean list values

# def clean_list(values):
#     cleaned = []
#     for v in values:
#         cleaned.append(v.strip().title())
#     return cleaned
# print(clean_list(["  MumBAi  ","  PuNe "]))


     
 
               
    
 