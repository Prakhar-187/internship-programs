print("List of months:January,February,March,April,May,June,July,August,September,October,November,December")
a=input("Input the month: ")
b=int(input("Enter day: "))

if(1<=b<=31 and (a=="March" or a=="April" or a=="May")):
   print("Season is Spring")
elif(1<=b<=31 and (a=="June" or a=="July" or a=="August")):
   print("Season is Summer")
elif(1<=b<=31 and (a=="September" or a=="October" or a=="November")):
   print("Season is autumn")
else:
   print("Season is winter")
   