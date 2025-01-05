a=int(input("Enter any number between 1500 to 2700: "))

if(1500<=a<=2700):
    if(a%7==0 and a%5==0 ):
        print("The number is divisible by 7 and 5")
    else:
        print("The number is not divisible by 7 and 5")
else:
    print("The number is not in range of 1500 to 2700")
