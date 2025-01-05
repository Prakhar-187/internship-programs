for i in range(1,8):
    if(i==1 or i==7):
        print("***")
    elif(i==2 or i==5 or i==6):
        print("*",end="")
        print(" ",end="")
        print("*",end="")
        print("")
    elif(i==4):
        print("****")
    else:
        print("*")
