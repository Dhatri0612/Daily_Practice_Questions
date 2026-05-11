numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Second Largest Number is:", numbers[-2])