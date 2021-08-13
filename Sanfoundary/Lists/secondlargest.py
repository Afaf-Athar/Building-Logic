arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("element to append: "))
    arr.append(num)
arr.sort()

print("Second Largest Number", arr[n-2])