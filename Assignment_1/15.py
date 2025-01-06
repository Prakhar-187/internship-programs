
password = input("Enter your password: ")
alphabet = 0
Capital = 0
Digit = 0
Special = 0


for i in password:

    if(i.islower()):
        alphabet+=1
    if(i.isdigit()):
        Digit+=1 
    if(i.isupper()):
        Capital+=1
    if(i=="$" or i=="#" or i=="@"):
        Special+=1
                  

if(alphabet>0 and Digit>0 and Special>0 and Capital>0 and 6<=len(password)<=16 ):
                print("Valid password")
else:
                print("Invalid password")
                