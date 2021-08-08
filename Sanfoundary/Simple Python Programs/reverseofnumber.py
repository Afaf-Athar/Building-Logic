def reverseofnum(n):
    # rev = 0
    # while(num>0):
    #     dig = num%10
    #     print(dig)
    #     rev = rev*10+dig
    #     num = num//2
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    print("Reverse of number", rev)


n = int(input("Enter the number: "))
reverseofnum(n)

# n=int(input("Enter number: "))4
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print("Reverse of the number:",rev)