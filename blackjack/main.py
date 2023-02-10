class Carta: 
    def __init__ (self, palo, valor):
        self.palo = palo
        self.valor = valor
    def __repr__ (self):
        return f"{self.valor} de {self.palo}"


if carta1.valor == 'reina':
    puntos = 10

valores=['as','2','3','4','5','6','7','8','9','10','J','reina','reai']
baraja=[]

for valor in valores:
    cartanueva = Carta('picas', valor)
    baraja.append(cartanueva)

for valor in valores:
    cartanueva = Carta('trevoles', valor)
    baraja.append(cartanueva)

for valor in valores:
    cartanueva = Carta('corazones', valor)
    baraja.append(cartanueva)

for valor in valores:
    cartanueva = Carta('diamentes', valor)
    baraja.append(cartanueva)


print(baraja)