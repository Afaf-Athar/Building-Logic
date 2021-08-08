def primefactorinteger(n):
    factors = []
    for i in range(n):
        if (i>1):
            if(n%i == 0):
                factors.append(i)
                k = 1
                for j in factors:
                    if(j% k == 0):
                        k = k+1
                if(k == 2):
                    print(j)


    # i = 1
    # while(i<=n):
    #     k = 0
    #     if (n%i == 0):
    #         j = 1
    #         while(j<=i):
    #             if(i%j == 0):
    #                 k = k+1
    #             j = j+1
    #         if(k == 2):
    #             print(i)
            
        i = i+1


n = int(input("Enter the Integer: "))
primefactorinteger(n)