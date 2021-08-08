def sumofposeveoddneg(arr):
    pos_even = 0
    pos_odd = 0
    neg = 0
    for i in arr:
        if(i>0):
            if(i%2 == 0):
                pos_even = pos_even + i
            else:
                pos_odd = pos_odd + i
        else:
            neg = neg + i
    print("Sum of all positive even numbers: ", pos_even)
    print("Sum of all positive odd numbers: ", pos_odd)
    print("Sum of all negative numbers: ", neg)



arr = []
n = int(input("Enter the number of elemets to be in list: "))
for i in range(n):
    a = int(input("Element: "))
    arr.append(a)

sumofposeveoddneg(arr)