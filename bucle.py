import random

numero= random.randint(1,1000)
numero2 = int(input('dime un numero: '))

while numero != numero2:
    if numero2 > numero:
        print('es demasiado grande')
    if numero2 < numero:
        print('es demasiado pequeño')
    numero2 = int(input('dime otro numero: '))

print('enhorabuena')