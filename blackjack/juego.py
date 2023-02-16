from baraja import Baraja
from mano import Mano
otra = True
otra2 = True

mibaraja = Baraja()
mano1= Mano()

mibaraja.mezclar()

carta_cogida= mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)


while otra == True :
    carta_cogida= mibaraja.coger_carta()
    mano1.añadir_carta(carta_cogida)

    mano1.mostrar_mano()
    mano1.calcula_valor()
    print(mano1.valor)

    if mano1.valor==21 :
        print('black jack!!!')
        break
    elif mano1.valor>21 :
        print('te has passado :(')
        otra2 = False
        break

    else:
        volver=input('quieres otra carta?')
        if volver == 'si':
             otra=True
        if volver == 'no':
             otra=False

print(' ')
mano_ordenador=Mano()

while otra2 == True :
    carta_cogida= mibaraja.coger_carta()
    mano_ordenador.añadir_carta(carta_cogida)
    mano_ordenador.calcula_valor()
    if mano_ordenador.valor > 21 :
        print('la banca ha hecho',mano_ordenador.valor)
        print('has ganado')
        break
    elif mano_ordenador.valor < mano1.valor:
        otra2 = True
    else:
        otra2 = False
        print('la banca ha hecho',mano_ordenador.valor)
        print('has perdido')




