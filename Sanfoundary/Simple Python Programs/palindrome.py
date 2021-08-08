def palindrome(n,copy):
    add = 0
    while(n>0):
        digit = n%10
        add = add * 10 + digit
        n = n//10
    if (add == copy):
        print("Palindrome Number")
    else:
        print ("Wrong")

n = int(input())
copy = n
palindrome(n,copy)