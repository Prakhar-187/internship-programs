import random

a=int(input("Enter number from 0 to 9: "))

b= random.randint(0,9)


number_of_guess=0
while(a!=b):
        print("Try Again!")

        number_of_guess +=1
        a=int(input("Enter number: "))
        
if(a==b):
        print("Correct Guess!")
        print(f"You took {number_of_guess} guesses to find answer")

        





    
    

