# security_code = int(input("Enter the security code : "))
# department = input("Enter the department : ")
# access_level = int(input("Enter the access level : "))
# if security_code == 5566:
#     if department == "Finance" :
#         if access_level >=5 :
#             print("Access Granted: Welcome to the meeting room.")
#         else:
#             print("Insufficient access level.")
#     else:
#         print("Access denied: Department not allowed.")
# else:
#     print("Invalid security code.")

# ASSIGNMENT 1:
# security_code = int(input("Enter the security code: "))
# if security_code == 5566:
#     department = input("Enter the department name :")
#     if department == "Finance" :
#         access_level =int( input("Enter the access level :"))
#         if access_level >= 5:
#             print("Access granted: Welcome to the meeting room.")
#         else:
#             print("Insufficient access level.")
#     else:
#         print("Access denied: Department not allowed.")
# else:
#     print("Invalid security code.")

# ASSIGNMENT 2:
# Create a program for Online Exam.
registration_number = int(input("Enter the registration number :"))
if registration_number == 1221:
    subject = input("Enter the subject name :")
    if subject.title() == "Python":
        password = int(input("Enter the password :"))
        if password == 8888:
            print("Login Successful! Start your exam.")
        else:
            print("Wrong password")
    else:
        print("Subject not avaialble")
else:
    print("Registration Failed")

        