

n = int(input("Enter a number to start with: "))
nums = []

for i in range(1,n + 1):
    num = float(input("Enter number {i}: ").format(i))
    nums.append(num)
print(f"List: {nums}")

avg = sum(nums)/n
print(f"Average: {avg}")

