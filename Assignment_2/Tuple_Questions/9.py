t=("w",1,"r","e","m","l","q","r","s","e")
l=list(t)
n=input("Enter element: ")

if(n in l):
    a=input("Element exists.\nFor removing press y else n: ")
    if(a=="y"):
        c=l.remove(n)
        print(tuple(l))
    elif(a=="n"):
        print(t)
    else:
        print(f"You entered something else. \n Here is your tuple as it is {t}")
else:
    print("Element not in tuple")
