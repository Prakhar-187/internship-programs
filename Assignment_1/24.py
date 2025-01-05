for i in range(0,7):
    for j in range(0,4):
        if((i==1 or i== 2) and (j==1 or j==2)):
            print(" ",end="")
        elif((i==4 or i==5 or i==6) and (j>=1)):
            print("   ",end="")
        else:
            print("*",end="")
    print("")