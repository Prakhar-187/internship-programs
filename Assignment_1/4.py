n=int(input("Enter any number: "))
for i in range(1,2*n):
    if(i<=n):
        print("*"*i,end="")
        print(""*(2*n-i))
    else:
        print("*"*(2*n-i),end="")
        print(""*i)