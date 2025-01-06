
for i in range (100,401):
    a=str(i)
    if (a[0] in "02468" and a[1] in "02468" and a[2] in "02468"):
        print(i)
    a=int(i/10)
    b=int(i/100)
    c=int(i)
    if(a%2==0 and b%2==0 and c%2==0):
        print(i,end=",")

