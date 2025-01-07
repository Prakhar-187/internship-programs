d1={1:10,2:20,3:30}
d2={4:50,5:60,6:70}
# d3=d1 | d2

for key,value in d2.items():
    d1[key]=value

print(d1)