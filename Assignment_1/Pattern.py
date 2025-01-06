n=int(input("Number: "))

for i in range(0,n+1):
    for k in range(n+1,i,-1):
        print(" ",end="")
    for j in range(0,i):
            print(" *",end="")
    print("")
    