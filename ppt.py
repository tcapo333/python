import random
repetir='si'
while repetir =='si' :
    usuario=input('piedra, papel o tijera? ')

    opciones = ['piedra','papel','tijera']
    ordenador= random.choice(opciones)
    print('el ordenador ha elegido '+ordenador)

    if usuario=='piedra' and ordenador=='tijera' :
        print('has ganador')
    if usuario=='piedra' and ordenador=='papel' :
        print('has perdido')

    if usuario=='papel' and ordenador=='piedra' :
        print('has ganador')
    if usuario=='papel' and ordenador=='tijera' :
        print('has perdido')

    if usuario=='tijera' and ordenador=='papel' :
        print('has ganador')
    if usuario=='tijera' and ordenador=='piedra' :
        print('has perdido')

    if usuario==ordenador :
        print('has empatado')

    repetir=input('quieres repetir? ')