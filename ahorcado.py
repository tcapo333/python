
import random
opciones=['patata', 'casa']
palabra_secreta= random.choice(opciones)

letras_correctas=[]
letras_incorrectas=[]
longitud_palabra=len(palabra_secreta)
seguir_jugando=True

while seguir_jugando==True:
    for letra in palabra_secreta:
        if letra in letras_correctas:
            print(letra, end="")
        else:
            print("_ ", end="")

    letra_pedida=input('\nletra: ')




    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)



    print('incorrectas',letras_incorrectas)
    print('correctas',letras_correctas)

    if set(letras_correctas) == set(palabra_secreta) :
        print('has ganado')
        seguir_jugando = False


    if len(letras_incorrectas) == 6:
        print('has perdido')
        print('la palabra era', palabra_secreta)
        seguir_jugando = False