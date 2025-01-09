sample={'1':['a','b'],'2':['c','d']}
l=[]
for values in sample.values():
    l.append(values)
# for i in range(0,2):
#         a=l[i]
# for j in range(0,2):
#         b=str(a)+l[i][j]

# print(b)
            
# print(l)
# print(l[0][0]+l[1][0])
# print(l[0][0]+l[1][1])
# print(l[0][1]+l[1][0])
# print(l[0][1]+l[1][1])
for i in range(0,2):
    first=l[i][i]

    for j in range(0,2):
     last=l[i][j]
# print(first+last)