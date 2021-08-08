def naturalnosummation(n):
    for i in range(1,n+1):
        s = []
        for j in range(1,i+1):
            print( j, sep = " ", end = " ")
            if(j<i):
                print("+",sep = " ",end =" ")
            s.append(j)
        print("=",sum(s))
    print()

n =int(input("Enter the number: "))
naturalnosummation(n)

# n=int(input("Enter a number: "))
# for j in range(1,n+1):
#     a=[]
#     for i in range(1,j+1):
#         print(i,sep=" ",end=" ")
#         if(i<j):
#             print("+",sep=" ",end=" ")
#         a.append(i)
#     print("=",sum(a))
 
# print()