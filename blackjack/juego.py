from baraja import Baraja
from mano import Mano

mibaraja = Baraja()
mano1= Mano()

mibaraja.mezclar()

carta_cogida= mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)

carta_cogida= mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)

carta_cogida= mibaraja.coger_carta()
mano1.añadir_carta(carta_cogida)

mano1.mostrar_mano()