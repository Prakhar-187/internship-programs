sample='w3resource'
l=[]
for i in range(0,len(sample)):
    l.append(sample[i])

d={}
for i in range(0,len(l)):
    d.update({l[i]:l.count(l[i])})
print(d)