print("List of months:January,February,March,April,May,June,July,August,September,October,November,December")
inputa = input("Enter month name: "):::
dict={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

if(inputa=="January" or inputa=="March" or inputa=="" or inputa==7 or inputa==8 or inputa==10 or input==12):
    print("No. of days: 31")
elif(inputa==2):
    print("No. of days: 28")
else:
    print("No. of days: 30")