# OOP's
# Create Object
# class student:
#     pass
# s1 = student()
# print(s1)

# Variable inside Class
# class student:
#     name = "Komal"
#     age = 28
# s1 = student()
# print(s1.name)
# print(s1.age)

# __init__() Constructor : It is an important topic
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# s1 = student("Komal",28)
# s2 = student("Abhishek",26)

# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)

# Methods in class
# class student:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print("My name is",self.name)
# s1 = student("Komal")

# s1.greet()

# # Class Car
# class car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#     def start(self):
#         print("My car brand is ",self.brand)
#         print("My car color is ",self.color)
# c1 = car("BMW","Black")

# c1.start()

# # Practice question
# # Create a Mobile class with:
# # brand
# # price
# # Print both values.

# class Mobile:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
# m1 = Mobile("Samsung",20000)
# print(m1.brand)
# print(m1.price)

# '''Create a Dog class with:
# name                        
# breed
# Create a method bark().'''
# class Dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#     def bark(self):
#         print("My dog name is ",self.name)
#         print("My dog breed is ",self.breed)
# d1 = Dog("Tommy","Husky")

# print(d1.name)
# print(d1.breed)

# d1.bark()

# Variable Inside Object
# class vehicle:
#     name = "Komal"
#     age = 28
# v1 = vehicle()
# print(v1.name)
# print(v1.age)

# Constructor
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
c1 = car("BMW","Black")
print(c1.brand)
print(c1.color)

# Method
class cat:
    def __init__(self,Breed,Color):
        self.Breed = Breed
        self.Color = Color
    def meow(self):
        print("My cat breed is ",self.Breed)
        print("My cat color is ",self.Color)
c1 = cat("persian","Black")
c1.meow()

# Create a dog class with name and breed and Craete a method Bark()
class dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(self.name,"is barking")
d1 = dog("Tommy","Labrador")
d1.bark()



        

        

        

        