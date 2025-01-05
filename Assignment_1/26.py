for i in range(1,8):
    if(i==1 or i==7):
        print("****")
    elif(i==2 or i==3):
        print("*")
    elif(i==4):
        print(" ",end="")
        print("***")
    else:
        print("  ",end="")
        print("*")