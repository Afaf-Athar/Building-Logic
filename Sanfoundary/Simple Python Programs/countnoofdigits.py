def countnoofdigits(n):
    count = 0
    while(n>0):
        count = count+1
        n = n//10
    print(count)

n = int(input("Enter the number: "))
countnoofdigits(n)