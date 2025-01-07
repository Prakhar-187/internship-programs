t=(1,2,3,4,5,6,7,8,9,10)
l=list(t)
half1=[]
half2=[]
for i in range (0,10):
    if(i<=4):
        half1.append(l[i])
    else:
        half2.append(l[i])
print(tuple(half1))
print(tuple(half2))
