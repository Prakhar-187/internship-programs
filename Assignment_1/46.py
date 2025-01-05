a=int(input("Enter first no.: "))
b=float(input("Enter second no.: "))
c=int(input("Enter third no.: "))

if(a>b and a>c):
    print("first no. is largest")
elif(b>a and b>c):
    print("second no. is largest")
elif(c>a and c>b):
    print("third no. is largest")
else:
    print("All are equal")