a=int(input("Enter tempterature in celsius: "))
def c_to_f():
   f = ((a*(9/5)) + 32)  #  °F = (°C × 9/5) + 32
   return f

print(f"{a}°C is {c_to_f()} in Farenhite")

print("")

b=int(input("Enter tempterature in farenhite: "))
def f_to_c():
  c=(5/9)*(b-32)
   # °C = 5/9(°F – 32)
  return c

print(f"{b}°F is {f_to_c()} in Celsiius")