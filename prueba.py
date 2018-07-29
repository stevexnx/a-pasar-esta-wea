import random
maquina = []
jugador1 = []
monton = []
colores = ["A","AM","V","R"]
valores = ["masDos"] + [v for v in range(2,11)] + ["MasC", "salto", "retorno","cambioColor"]
valores = ["masDos"] + [v for v in range(2,10)] + ["MasC", "salto", "retorno","cambioColor"]
baraja = [(valor, color ) for color in colores for valor in valores]
print(baraja)
# print(baraja)
def aleatorio (mazo):
    listaA = []
    for i in range(0,52):
        carta = random.choice(mazo)
        listaA.append(carta)
        mazo.remove(carta)
    return listaA

baraja = aleatorio(baraja)
# print (baraja)

# print ("Aleatorias xd:" , baraja)
#print (baraja[1])
print (len(baraja))

def repartir(jugador):
    for i in range(7):
        jugador.append(baraja.pop())
    return jugador

turno = int(input("Elige quien comieza \n 1) Para comenzar tu \n 2) Para la maquina \n : "))

jugador1 = repartir(jugador1)
maquina = repartir(maquina)
print(jugador1 , "\n" ,maquina)
# print (len(baraja))
# print(baraja)
monton.append(baraja[-1])
baraja.remove(monton[0])
# print(monton)
# print(baraja)