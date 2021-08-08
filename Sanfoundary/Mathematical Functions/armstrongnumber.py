def armstrongnumber(n):
    temp = n
    s= 0
    while(temp>0):
        div = temp % 10
        s = s + (div * div * div)
        temp = temp//10
    if(s == n):
        print("It is an Armstrong number")
    else:
        print("Not an Armstring number")



n = int(input("Enter the number: "))
armstrongnumber(n)