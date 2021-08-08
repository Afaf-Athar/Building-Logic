def rangeofvalues(limit):
    for i in range(0,limit+1):
        if(i%2 != 0 and i%3 != 0):
            print(i)

limit = int(input("Enter limit: "))
rangeofvalues(limit)
