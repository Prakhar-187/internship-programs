print("Enter 0 when done typing numbers.")
a=int(input("Enter numbers: "))

l=[]


while (a!=0) :
    a=int(input("Enter numbers: "))

    l.append(a)

E=0
O=0

for i in range(0,len(l)):
    if(l[i]%2==0):
        E=E+1
    else:
        O=O+1

print(f"Number of even numbers: {E}")
print(f"Number of odd numbers: {O}")






