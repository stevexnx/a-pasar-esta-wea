colores = ["A","AM","V","R"]
valores = ["masDos"] + [v for v in range(2,11)] + ["MasC", "salto", "retorno","cambioColor"]
baraja = [(valor, color ) for color in colores for valor in valores]
print(baraja)