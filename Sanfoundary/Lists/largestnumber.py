arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("element to append: "))
    arr.append(num)
arr.sort()

print("Largest Number", arr[n-1])