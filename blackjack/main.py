

valores=['as','2','3','4','5','6','7','8','9','10','J','reina','reai']
palos=['picas','corazones','treboles','diamantes']
baraja=[]

for palo in palos:
    for valor in valores:
        cartanueva = Carta(palo, valor)
        baraja.append(cartanueva)

print(baraja)