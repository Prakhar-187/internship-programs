for i in range(0,7):
    for j in range(0,5):
        if(i != 6 and j==2 or j==1 or j==3):
            print(" ",end="")
        else:
            print("*",end="")
    print("")