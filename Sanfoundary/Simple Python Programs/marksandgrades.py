def marksandgrades(sub1,sub2,sub3,sub4,sub5):
    avg = (sub1+sub2+sub3+sub4+sub5)/5
    if(avg>=90):
        print("Grade A")
    elif(avg>=80 and avg <90):
        print("Grade B")
    elif(avg>=70 and avg <80):
        print("Grade C")
    elif(avg>=60 and avg <70):
        print("Grade D")
    elif(avg>=50 and avg <60):
        print("Grade E")
    else:
        print("Work Hard")

a = int(input("Grade for sub1: "))
b = int(input("Grade for sub2: "))
c = int(input("Grade for sub3: "))
d = int(input("Grade for sub4: "))
e = int(input("Grade for sub5: "))
marksandgrades(a,b,c,d,e)