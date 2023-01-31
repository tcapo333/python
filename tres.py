import random
casillas=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
otra=true
print('''
    | | | |
    | | | |
    | | | |
    ''')
while seguir == true :
    while otra == true
        posicion=int(input('elige una casilla del 0 al 8: '))
        if casillas[posicion]==' '
            casillas[posicion]='X'
            otra=false
            print(
                '|'+casillas[0]+'|'+casillas[1]+'|'+casillas[2]+'|\n' 
                '|'+casillas[3]+'|'+casillas[4]+'|'+casillas[5]+'|\n'
                '|'+casillas[6]+'|'+casillas[7]+'|'+casillas[8]+'|\n'    
                )
        else posicion=int(input('elige una casilla del 0 al 8: '))
            otra=true

    posicion=random.randint(0,8)

    casillas[posicion]='O'
    print(
        '|'+casillas[0]+'|'+casillas[1]+'|'+casillas[2]+'|\n' 
        '|'+casillas[3]+'|'+casillas[4]+'|'+casillas[5]+'|\n'
        '|'+casillas[6]+'|'+casillas[7]+'|'+casillas[8]+'|\n'    
        )

    if casillas[0]==casillas[1]==casillas[2]=='X'
        print('has ganado')
        seguir=false
    if casillas[0]==casillas[1]==casillas[2]=='O'
        print('has perdido')
        seguir=false
    if casillas[3]==casillas[4]==casillas[5]=='X'
        print('has ganado')
        seguir=false
    if casillas[3]==casillas[4]==casillas[5]=='O'
        print('has perdido')
        seguir=false
    if casillas[6]==casillas[7]==casillas[8]=='X'
        print('has ganado')
        seguir=false
    if casillas[6]==casillas[7]==casillas[8]=='O'
        print('has perdido')
        seguir=false
    if casillas[0]==casillas[3]==casillas[6]=='X'
        print('has ganado')
        seguir=false
    if casillas[0]==casillas[3]==casillas[6]=='O'
        print('has perdido')
        seguir=false
    if casillas[1]==casillas[4]==casillas[7]=='X'
        print('has ganado')
        seguir=false
    if casillas[1]==casillas[4]==casillas[7]=='O'
        print('has perdido')
        seguir=false
    if casillas[2]==casillas[5]==casillas[8]=='X'
        print('has ganado')
        seguir=false
    if casillas[2]==casillas[5]==casillas[8]=='O'
        print('has perdido')
        seguir=false
    if casillas[0]==casillas[4]==casillas[8]=='X'
        print('has ganado')
        seguir=false
    if casillas[0]==casillas[4]==casillas[8]=='O'
        print('has perdido')
        seguir=false
    if casillas[2]==casillas[4]==casillas[6]=='X'
        print('has ganado')
        seguir=false