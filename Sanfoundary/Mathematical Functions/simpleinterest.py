def simpleinterest(p,r,t):
    simpleinterestcal = float((p*r*t)/100)
    print(simpleinterestcal)


p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate: "))
t = int(input("Enter the time: "))
simpleinterest(p,r,t)