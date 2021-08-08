def minimumdivisor(n):
    L = []
    for i in range(2,n):
        if(n%i == 0):
            L.append(i)
    print(min(L))

n = int(input("Enter the number: "))
minimumdivisor(n)