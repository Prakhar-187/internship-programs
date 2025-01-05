
a=input("Enter: ")::::
b=int(a)
Digits =0
Letters = 0
for i in range(0,len(a)+1):
    if(b[i]==1 or b[i]==2 or b[i]==3 or b[i]==4 or b[i]==5 or b[i]==6 or b[i]==7 or b[i]==8 or b[i]==9 or b[i]==0):
        Digits+=1
    else:
        Letters+=1
print(f"Digits: {Digits}\nLetters: {Letters}")