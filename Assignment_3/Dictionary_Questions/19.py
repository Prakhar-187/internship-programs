d1={'a':100,'b':200, 'c':300}
d2={'a':200, 'b':300,'d':400}

l1key=list(d1.keys())
l2key=list(d2.keys())

l1value=list(d1.values())
l2value=list(d2.values())

d3={}
for i in range(0,3):
    if(l1key[i]==l2key[i]):
        a=l1value[i]+l2value[i]
        d3[l1key[i]]=a
    else:
        d3[l1key[i]]=l1value[i]
        d3[l2key[i]]=l2value[i]

print(d3)
