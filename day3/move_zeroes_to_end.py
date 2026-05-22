num = [1, 0, 2, 0, 4, 0, 5]
result = []
zero_count = 0
for i in num:
    if i != 0:
        result.append(i)
    else:
        zero_count += 1

for i in range(zero_count):
    result.append(0)

print(result)