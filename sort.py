arr = [100, 2, 20, 5, 9, 8, 7]

for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[i]:
            arr[j], arr[i] = arr[i], arr[j]

print(arr)


"""
9 8 7 => 7 8 9

if i = 9 > j = 8 : true, then exchange
8, 9, 7
if 8 > 9 false
9 7 true
8 7 9
8 7 true
7 8 9



"""
