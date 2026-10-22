import math
cateto1 = float(input("dime el cateto 1: "))
cateto2 = float(input("dime el cateto 2: "))
if cateto1 <=0 or cateto2 <=0:
    print("ningun numero puede ser menor o igual que 0")
else:
    h = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    print("La hipotenusa es", h)