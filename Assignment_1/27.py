for i in range(0,7):
    for j in range(0,5):
        if((i==2 or i==3 or i==4 or i==5 or i==6 or i==1) and (j==1 or j==3 or j==4 or j==5 or j==0)):
            print("   ",end="")
        else:
            print(" * ",end="")
    print("")