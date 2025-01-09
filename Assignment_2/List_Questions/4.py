sample=[12,15,11,12,8,15,3,3]
print(sample)

diff_list=[]
same_list=[]

for i in range (0,len(sample)):
    if(sample.count(sample[i]) > 1):
#         sample.remove(sample[i])
#         # len(sample)-=len(sample)

# print(sample)
        if(sample[i] in same_list):
            continue
        else:
            same_list.append(sample[i])
    else:
        diff_list.append(sample[i])

unique_list = diff_list + same_list

print(f"unique items: {unique_list}")

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





