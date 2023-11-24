# size = int(input("Enter the size of storage: "))

# Array = []
# for i in range(1, size+1):
#     Array.append(int(input(f"Array[{i}]: ")))

# search = int(input("Search number: "))

search = 3
Array = [1, 2, 3, 200]
for i in range(len(Array)):
    print(i)
    if (Array[i] == search):
        print(f"{Array[i]} is in Array[{i+1}]")
        break
    # else:
