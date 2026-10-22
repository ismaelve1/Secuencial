import math
base = float(input("dime la base del rectangulo: "))
altura = float(input("dime la altura del rectangulo: "))

if base <= 0 or altura <= 0:
    print("ningun numero puede ser menor o igual a cero")
else:
    area = base * altura
    perimetro = 2 * (base + altura)

    print("el area del rectangulo es", area)
    print("el perimetro del rectangulo es", perimetro)