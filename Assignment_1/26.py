for i in range (0,7):
    for j in range (0,5):
        if(i==0 or i==6 or ((0<i<4) and j==0) or ((3<i<6) and j==4) or (i==3)):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    