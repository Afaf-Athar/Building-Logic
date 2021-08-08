def sumofdigits(n):
    s = 0
    while(n>0):
        dig = n%10
        s = s + dig
        n = n//10
    print (s)

n =int(input("Enter the digit :"))
sumofdigits(n)