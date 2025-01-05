

# for i in range(0,7):
#     for j in range(0,5):
#         if(i==0 or i==3 or j==0 or ((i==1 or i==2) and j==4) or ((i>3)and(j==i-2))) :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

n=int(input("Number: "))
for i in range(0,n):
    for j in range(0,n-2):
        if(n%2==0):
            if(i==0 or i==n/2 or j==0 or ((0<i<n/2) and j==n-3) or ((i>n/2)and(j==i-2))) :
                print("*",end="")
            else:
                print(" ",end="")

        else:
            if(i==0 or i==(n-1)/2 or j==0 or (((0<i<(n-1)/2) and j==n-3) or ((i>(n-1)/2)and(j==i-2)))):
                        print("*",end="")
            else:
                        print(" ",end="")

        # else:
        #     if(i==0 or i==(n-1)/2 or j==0 or ((i==((n-1)/2)-1 or i==((n-1)/2)-2 and j==n-2) or ((i>n/2)and(j==i-2)))):
        #         print("*",end="")
        #     else:
        #         print(" ",end="")
    print("")

    


    # i==((n-1)/2)-1 or i==((n-1)/2)-2)