list1=[3,6,9,12,15,18,21]
list2=[4,8,12,16,20,24,28]

odd_list1=[]

for i in range(1,int(len(list1)/2+1)):
    odd_list1.append(list1[2*i-1])

print(f"Element at odd index position from list 1\n {odd_list1}")

even_list2=[]
for j in range(0,int(len(list2)/2)+1):
    even_list2.append(list2[2*j])

print(f"Element at even index position from list 2\n {even_list2}")

final_list=odd_list1+even_list2

print(f"Printing Final third list\n {final_list}")