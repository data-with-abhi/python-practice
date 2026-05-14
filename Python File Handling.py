# 1 Reading Full File
# with open("sample.txt","r") as f:
#     print(f.read())

# with open("sample.txt","r") as f:
#     for line in f:
#         print(line.strip().title())

# Writing
with open("notes.txt","w") as f:
    f.write("Day 20 - File Handling\n")
    f.write("Reading and Writing\n")

# Appending
with open("notes.txt","a") as f:
    f.write("Appending new line\n")

# Cleaning Data in files
Cleaned = []
with open("sample.txt","r") as f:
    for line in f:
        Cleaned.append(line.strip().title())
with open("cleaned_output.txt","w") as f:
    for city in Cleaned:
        f.write(city + "\n")

# Counting Lines
count = 0
with open("sample.txt","r") as f:
    for _ in f:
        count+=1
    print("Total lines",count)

with open("notes.txt","w") as f:
    f.write("Line is Busy \n")
    f.write("Line by line \n")
    f.close()

with open("sample.txt","r") as f:
    print(f.read())

with open("sample.txt","r") as f:
    for line in f:
        print(line.strip().title())
    

