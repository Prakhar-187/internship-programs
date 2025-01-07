lis1=["Mike","","Emma","Kelly","Brad"]
for i in range(1,len(lis1)):
    if(lis1[i-1]==""):
        lis1.remove(lis1[i-1])

print(lis1)