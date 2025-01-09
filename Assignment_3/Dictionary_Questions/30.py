sample={'item1':45.5,'item2':35,'item3':41.3,'item4':55,'item5':24}
lvalues=[]
lkeys=[]

# for y in sample.keys():
#     lkeys.append(y)
# # print(lkeys)

sorted_sample={}
for x in sample.values():
    lvalues.append(x)
lvalues.sort()
# print(lvalues)

for i in range(len(lvalues)-4,len(lvalues)-1):
    sorted_sample.update({:lvalues[i]})
print(sorted_sample)