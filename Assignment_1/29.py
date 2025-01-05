for i in range(1,8):
    if(i==4):
        print("  ",end="")
        print("*",end="")
        print("  ")
    elif(i==3 or i==5):
        print(" ",end="")
        print("*",end="")
        print(" ",end="")
        print("*",end="")
        print(" ")
    else:
        print("*",end="")
        print(" ",end="")
        print(" ",end="")
        print(" ",end="")
        print("*")