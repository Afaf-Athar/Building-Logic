def invertedstar(n):
    for i in range(n,0,-1):
        print((n-i) * " " + i * "*")


n =int(input("Enter the number: "))
invertedstar(n)

 