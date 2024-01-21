

nums = []
evennum = []
while True:
    user_input = input("Enter an integer ('QUIT' to stop the program): ")

    if user_input.upper() == "QUIT":
        break

    num = int(user_input)
    nums.append(num)

    if num % 2 == 0:
        evennum.append(num)

print("All nums:"+str(nums))
print("Even nums:"+str(evennum))

