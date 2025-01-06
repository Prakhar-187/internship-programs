n=int(input("Enter integer number: "))
l=[]
l.append(n)

while(n!=0):
    n=int(input("Enter integer number: "))
    l.append(n)

sum=0
avg = 0
for i in range (0,len(l)):
    sum=(l[i]) + sum
    
print(sum)
avg = sum/(len(l)-1)
print(avg)