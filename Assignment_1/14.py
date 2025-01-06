
a=input("Enter: ")
Digits =0
Letters = 0
Special_Char = 0

for i in a:
    if(i.isdigit()):
        Digits+=1
    elif(i.isalpha()):
        Letters+=1
    else:
        Special_Char+=1

print(f"Digits : {Digits}")
print(f"Letters : {Letters}")
# print(f"Special Characterstics : {Special_Char}")


