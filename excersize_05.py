

print("Enter 5 ints: ")

list1 = []
list2 = []

for i in range(5):
    list1.append(int(input()))

print("Enter 5 ints")
for i in range(5):
    list2.append(int(input()))

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)

print("List 1 "+str(list1)) 
print("List 2 "+str(list2))       
print("Common List" +str(list3))

