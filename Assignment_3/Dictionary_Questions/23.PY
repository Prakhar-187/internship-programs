sample=[{'item':'item1','amount':400},{'item':'item1','amount':750},{'item':'item2','amount':300}]
# print(sample[0].values())

new={}
a=0
for i in range(0,3):
    for x in sample[i].values():          
        if 'item1' in sample[i].values():
            if 'amount' in sample[i].keys():
                a+=sample[i]['amount']
            new.update({'item1':a})                
        else:
            new.update({'item2':x})
print(new)