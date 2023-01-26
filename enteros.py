import math
a = float(input("dime a numero: "))
b = float(input("dime b numero: "))
c = float(input("dime c numero: "))
disc = (b**2)-(4*a*c)

if disc < 0 :
    print("no tiene solucion")

else:
    print((-b+math.sqrt(b**(2)-4*a*c))/(2*a))
    print((-b-math.sqrt(b**(2)-4*a*c))/(2*a))