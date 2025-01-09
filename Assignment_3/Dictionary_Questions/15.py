d2={6:70,4:50,8:80,5:60,7:90}
l1=list(d2.values())
min=0
max=0
for i in range (1,5):
    if(l1[i-1]<l1[i]):
        min=l1[i-1]
    if(l1[i-1]>l1[i]):
        max=l1[i+1]
print(min)
print(max)