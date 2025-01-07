sl=[12,15,11,12,8,15,3,3]
print(len(sl))
unique_list=[]
for i in range(0,len(sl)):
    if(sl.count((sl[i])>1)):
        unique_list.append(sl[i])
        sl.remove(sl[i])
        # unique_list.append(sl[i])

    elif((sl.count(sl[i])==1)):
        unique_list.append(sl[i])
        continue
        
print(unique_list)