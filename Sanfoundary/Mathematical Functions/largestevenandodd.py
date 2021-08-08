def largestevenandodd(arr):
    large_eve = []
    large_odd = []
    for i in arr:
        if(i%2 == 0):
            large_eve.append(i)
        else:
            large_odd.append(i)
    
    large_eve.sort()
    large_odd.sort()
    print("The largest even ", large_eve[-1])
    print("The largest odd ", large_odd[-1])
    
arr = []
n =int(input("Enter the number of elemets: "))
for i in range(n):
    a = int(input(" Enter the element: "))
    arr.append(a)

largestevenandodd(arr)