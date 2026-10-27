v1 = float(input("dime la velocidad del primer coche (km/h):"))
v2 = float(input("dime la velocidad del segundo coche (km/h):"))
dist = float(input("dime la distancia entre los coches (km):"))

tiempo = dist / abs(v1 - v2)
tiempo = tiempo * 60

print("lo alcanzara en",tiempo,"minutos")
