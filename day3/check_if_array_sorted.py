num= [1, 2, 3, 4, 5]
sorted_array = True
for i in range(len(num)-1):
    if num[i] > num[i+1]:
        sorted_array = False
        break

if sorted_array:
    print("Sorted")
else:
    print("Not Sorted")