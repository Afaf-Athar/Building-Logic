def rangeof5and7(lower,upper):
    for i in range(lower,upper+1):
        if(i%5 == 0 and i%7 == 0):
            print(i)

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
rangeof5and7(lower,upper)