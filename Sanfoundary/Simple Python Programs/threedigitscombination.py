def threedigitscombination(num1,num2,num3):
    d = []
    d.append(num1)
    d.append(num2)
    d.append(num3)
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j and j!=k and k!=i):
                    print(d[i],d[j],d[k])


num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
threedigitscombination(num1,num2,num3)

