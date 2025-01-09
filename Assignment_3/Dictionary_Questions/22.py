d2={6:70,4:50,8:80,5:60,7:90,2:20}
l2=list(d2.keys())
l2.sort()
a=l2[-4:-1]
print(a)

for key in a:
    if key in d2:
        value=d2[key]
        print(f"{key}:{value}")



