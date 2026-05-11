l = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for num in l:
    if num not in unique_list:
        unique_list.append(num)
print("Unique List : ",unique_list)
