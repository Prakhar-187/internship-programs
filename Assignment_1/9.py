
n=int(input("Enter number till which you want fibonacci series: "))

def fibo():
    a=0
    b=1
    c=a+b
    print(a)
    print(b)
    for i in range(0,n-2): 
        print(c)
        a=b
        b=c
        c=a+b

fibo()
        





