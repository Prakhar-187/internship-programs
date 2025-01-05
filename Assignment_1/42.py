n=int(input("Enter integer number: "))::
l=[]

while(n!=0):
    n=int(input("Enter integer number: "))
    l.append(n)

for i in range (1,l[-1]):
    sum=l[0]+l[i]
    avg=(l[0]*l[i])/len(l)
print(sum)
print(avg)