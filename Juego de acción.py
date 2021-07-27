import random

turno = random.randint(1,2)
print(turno)

P1vida = 100
P2vida = 100
P1daño = 50
P2daño = 20
nombre=input("Elige el nombre de tu personaje: ")

while P1vida > 0 and P2vida > 0:
    
    if turno == 1:
        P2vida = int(P2vida) - int(P1daño)
        print("-",nombre, "le hizo ",P1daño," de daño a jugador 2" )
        print("  Jugador 2 tiene", P2vida,"de vida\n")
        turno = 2
        
    else:
        P1vida = int(P1vida) - int(P2daño)
        print("- Jugador 2 te hizo", P2daño ,"de daño" )
        print(" ",nombre,"tiene", P1vida,"de vida\n")
        turno = 1
        
if P1vida <= 0:
    print("El jugador 2 ganó")
else:
    print(nombre +" ganó")