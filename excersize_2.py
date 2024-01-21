user_input = input("Enter a string: ")
lowerCase = ""
upperCase = ""
for one in user_input:
    if one.isupper():
        upperCase += one
    elif one.islower():
        lowerCase += one
completeStr = lowerCase + upperCase
print(completeStr)