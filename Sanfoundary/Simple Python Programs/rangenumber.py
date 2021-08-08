def rangenumber(lower,upper,n):
    for i in range(lower,upper+1):
        if(i%n == 0):
            print(i)

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
n = int(input("Enter number: "))
rangenumber(lower,upper,n)