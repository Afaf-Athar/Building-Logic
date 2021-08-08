def leapyear(n):
    if(n%4 == 0 and n%100 != 0 or n%400 == 0):
        print("It's a leap year")
    else:
        print("It's not a leap year")

n = int(input("Enter the year: "))
leapyear(n)