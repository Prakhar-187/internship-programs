a=int(input("Enter year: "))

if(a%4==0 and a%100 != 0):
    print("It is leap year")
elif(a%400==0):
    print("It is leap year")
else:
    print("It is not leap year")
