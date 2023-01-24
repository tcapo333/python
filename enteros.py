import math
a = int(input("dime un numero: "))
b = int(input("dime otro numero: "))
c = int(input("dime otro numero: "))

print((-b+math.sqrt(b**(2)-4*a*c))/(2*a))
print((-b-math.sqrt(b**(2)-4*a*c))/(2*a))