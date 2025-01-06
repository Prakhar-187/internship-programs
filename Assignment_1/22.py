# for i in range (0,7):
#     for j in range (0,5):
#         if(j==0 or j==4 or (i==3 and j==2) or (i==2 and (j==1 or j==3))):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

n=int(input("Enter rows: "))

for i in range (0,n):
    for j in range (0,n-2):
            if(j==0 or j==n-3 or (i==((n-1)/2) and j==((n-3)/2))):
                print("*",end="")
            else:
                print(" ",end="")
    print("")



    # or (i==((n-3)/2) and (j==((n-)) or j==3))