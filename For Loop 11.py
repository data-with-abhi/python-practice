# # For Loop
# # Basic Loop
# for i in range(1,11):
#     print(i)

# # Print Chararcters
# word = "Python"
# for alphabet in word:
#     print(word)

# name = "Komal"
# for i in range(1,6):
#     print(name)

# word2 = "Python"
# for letter in word2:
#     print(word2)
# for j in word2:
#     print(j)

# word3 = "SQL"
# for k in range(1,11):
#     print(word3)

# word4 = "Komal I LOVE YOU TOO"
# for l in range(1,1001):
#     print(word4)

# # Loop through list
# items = ["Pen","Book","Laptop"]
# for item in items:
#     print(item)
# for o in range(1,5):
#     print(items)

# # Even Numbers
# print("Even Numbers")
# for i in range(0,21,2):
#     print(i)

# print("Odd Numbers")
# for i in range(1,21,2):
#     print(i)

# # Total Calculation
# marks = [78,82,90,95,65,78,65]
# total = 0
# for m in marks:
#     total += m
# print("Total :",total)

# # Clean City Names
# cities = ["  MUMBAI","PuNe  ","  CHENNAI "]
# cleaned = []
# for c in cities:
#     cleaned.append(c.strip().title())
# print(cleaned)

# # Clear Country names
# country = ["  luXemBerG  ","ameriCA   ","   JaPaN"]
# cleared = []
# for co in country:
#     cleared.append(co.strip().title())
# print(cleared)

# # Loops with If Condition
# nums = [2,18,1,4,12,19]
# for n in nums:
#     if n>=10:
#         print(n,"is greater")
#     else:
#         print(n,"is smaller")

# # Loops with If condition
# nums = [2,18,1,4,12,19]
# for n in nums:
#     if n%2==0:
#         print(n,"Even Numbers")
#     else:
#         print(n,"Odd Numbers")

# # Extract last four digit number
# emp_code = ["Emp-001999","Emp-998786"]
# for e in emp_code:
#     print(e[-4:])
#     print(e[4:7][::1])

# # Fixing Spelling Mistakes
# wrong_list = ["Bengluru","Mombai","Kolkatta"]
# correct = []
# for fix in wrong_list:
#     correct.append(fix.replace("Bengluru","Bengaluru")
#                    .replace("Mombai","Mumbai")
#                    .replace("Kolkatta","Kolkata"))
# print(correct)

# # looping through dictionary
# student = {"name":"Komal","age":28,"city":"Pune"}
# for key,value in student.items():
#     print(key,":",value)