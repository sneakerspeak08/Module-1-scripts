

inputs = []
ct = {}
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    inputs.append(num)
    if num in ct:
        ct[num] += 1
    else:
        ct[num] = 1

unique_elements = []

for num, count in ct.items():
    if count == 1:
        unique_elements.append(num)
print(f"Original list: {inputs}")
print(f"List of unique elements: {unique_elements}")

