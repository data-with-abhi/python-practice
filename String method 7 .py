# Python String Method
# Remove Spaces
text1 ="      hello python learner  "
print("Remove Spaces :",text1.strip())

# Convert into capital letter
print("Upper Letter :",text1.upper().strip())

#Convert into Proper case
print("Proper case :",text1.title().strip())

# Replace
print("Replace word python with SQL :",text1.replace("python","SQL").strip())

# Count occurence of a letter
print("Count of o :",text1.count("o"))

# Check if text is starts with something
print("Check the text is start with hello ?",text1.strip().startswith("hello"))

#Check if only numbers are present in data
value = "9621622169"
print("Check if the numeric is present",value.isnumeric())

#Split string into list of words
msg= "Welcome to python course"
words = msg.split()
print("Split the word :",words)

#Join back with hyphen
joined_text = "-".join(words)
print("Joined text :",joined_text)

#Find position of letter
print("find Index of P : ",msg.find("p"))

# Find Domain
email = "singhshekabhi099@gmail.com"
domain = email[email.find("@")+1:]
print("Find Domain :",domain)

# Advance example: Clean Price (Remove Soecial Characters)
#Example: "Price: Rs 3500/- "3500"
price_text = "Price: Rs 3500/-"
Clean_price = price_text.replace("Price:"," ").replace("Rs"," ").replace("/-"," ")
print("Print only 3500 :",Clean_price)