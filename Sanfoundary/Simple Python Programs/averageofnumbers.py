n = int(input("Enter no of elements: "))
l = []
for i in range(n):
    ele = int(input())
    l.append(ele)

avg = sum(l)/n
print(round(avg,2))