import random
casillas=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista=[0,1,2,3,4,5,6,7,8]
seguir = True
turnos = 9
print('''
    | | | |
    | | | |
    | | | |
    ''')

while seguir == True :
    
    posicion=int(input('elige una casilla del 0 al 8: '))
    if casillas[posicion] == ' ' :
     casillas[posicion]='X'
     lista.remove(posicion)
     print('|'+casillas[0]+'|'+casillas[1]+'|'+casillas[2]+'|\n' '|'+casillas[3]+'|'+casillas[4]+'|'+casillas[5]+'|\n' '|'+casillas[6]+'|'+casillas[7]+'|'+casillas[8]+'|\n')
    else:  
        posicion=int(input('elige una casilla que no este ocpuada del 0 al 8: ')) 
        casillas[posicion]='X'
        lista.remove(posicion)

    if casillas[0]==casillas[1]==casillas[2]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[1]==casillas[2]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[3]==casillas[4]==casillas[5]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[3]==casillas[4]==casillas[5]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[6]==casillas[7]==casillas[8]=='X':
        print('has ganado')
        seguir=False
        break
    if casillas[6]==casillas[7]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[0]==casillas[3]==casillas[6]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[3]==casillas[6]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[1]==casillas[4]==casillas[7]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[1]==casillas[4]==casillas[7]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[2]==casillas[5]==casillas[8]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[2]==casillas[5]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[0]==casillas[4]==casillas[8]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[4]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[2]==casillas[4]==casillas[6]=='X' :
        print('has ganado')
        seguir=False
        break
    turnos=turnos-1
    if turnos == 0:
        break

    posicion=random.choice(lista)
    lista.remove(posicion)
    casillas[posicion]='O'
    print(
        '|'+casillas[0]+'|'+casillas[1]+'|'+casillas[2]+'|\n' 
        '|'+casillas[3]+'|'+casillas[4]+'|'+casillas[5]+'|\n'
        '|'+casillas[6]+'|'+casillas[7]+'|'+casillas[8]+'|\n'    
        )

    if casillas[0]==casillas[1]==casillas[2]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[1]==casillas[2]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[3]==casillas[4]==casillas[5]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[3]==casillas[4]==casillas[5]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[6]==casillas[7]==casillas[8]=='X':
        print('has ganado')
        seguir=False
        break
    if casillas[6]==casillas[7]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[0]==casillas[3]==casillas[6]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[3]==casillas[6]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[1]==casillas[4]==casillas[7]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[1]==casillas[4]==casillas[7]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[2]==casillas[5]==casillas[8]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[2]==casillas[5]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[0]==casillas[4]==casillas[8]=='X' :
        print('has ganado')
        seguir=False
        break
    if casillas[0]==casillas[4]==casillas[8]=='O' :
        print('has perdido')
        seguir=False
        break
    if casillas[2]==casillas[4]==casillas[6]=='X' :
        print('has ganado')
        seguir=False
        break
    
    turnos=turnos-1
    if turnos == 0: 
        break
        print('has empatado')
        
