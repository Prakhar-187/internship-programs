year=int(input("Input year: "))
month=int(input("Input month[1-12]: "))
day=int(input("Input date[1-31]: "))

if(year%4==0 and year%100!=0):
    if(month==2 and day==28):
        print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day+1}")
    elif(month==2 and day==29):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-28}")

    elif(month==12 and day==31 ):
        print(f"The next date is [yyyy-mm-dd] {year+1}-{month-11}-{day-30}")

    elif(month==2 and day==28 ):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-27}")

    elif(month == 1 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
    elif(month == 3 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
    elif(month == 5 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
    elif(month == 7 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")      
    elif(month == 8 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
    elif(month == 10 and day==31):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")

    elif( month == 4 and day == 30):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
    elif( month == 6 and day == 30):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
    elif( month == 9 and day == 30):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
    elif( month == 11 and day == 30):
            print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
        
    else:
            print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day+1}")
        

elif(month==12 and day==31 ):
        print(f"The next date is [yyyy-mm-dd] {year+1}-{month-11}-{day-30}")

elif(month==2 and day==28 ):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-27}")

elif(month == 1 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
elif(month == 3 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
elif(month == 5 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
elif(month == 7 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")      
elif(month == 8 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")
elif(month == 10 and day==31):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-30}")

elif( month == 4 and day == 30):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
elif( month == 6 and day == 30):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
elif( month == 9 and day == 30):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
elif( month == 11 and day == 30):
        print(f"The next date is [yyyy-mm-dd] {year}-{month+1}-{day-29}")
      
else:
        print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day+1}")
       