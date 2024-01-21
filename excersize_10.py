

string = input("Enter a string:")
list = list(string)
splitlist = [list[i:i + 3] for i in range(0, len(list), 3)]

print(splitlist)

