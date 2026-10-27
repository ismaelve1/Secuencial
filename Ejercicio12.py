import math
print("escribe las coordenadas del punto 1:")
x1 = float(input("dime x1: "))
y1 = float(input("dime y1: "))
print("escribe las coordenadas del punto 2:")
x2 = float(input("dime x2: "))
y2 = float(input("dime y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("la distancia entre los puntos es:", distancia)