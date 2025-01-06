sample=[12,15,11,12,8,15,3,3]
print(sample)
unique_list=[]

for i in range (1,len(sample)-1):
    if i  in sample:
        continue
    else:
        unique_list.append(sample[i])

print(f"unique items: {unique_list}",end=",")

t=tuple(unique_list)
print(f"tuple: {t}" )

min=0
max=0

for j in range(1,len(unique_list)):
    if(unique_list[j-1]>unique_list[j]):
        min=unique_list[j]

print(min)

for k in range(1,len(unique_list)):
    if(unique_list[j-1]>unique_list[j]):
        max=unique_list[j-1]

print(max)





