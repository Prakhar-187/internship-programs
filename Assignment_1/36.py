print("Input length of triangle sides")
a=int(input("x: "))
b=int(input("y: "))
c=int(input("z: "))

if(a==b==c):
    print("Equilateral triangle")
elif(a==b!=c):
    print("Scalene traingle")
else:
    print("Isosceles traingle")