n=int(input("Enter number: "))
d1={}

for i in range (1,n+1):
    d1.update({i:i**2})
print(d1)