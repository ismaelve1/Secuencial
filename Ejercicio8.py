sueldobase = float(input("dime el sueldo base:"))

venta1 = float(input("dime el precio de la primera venta: "))
venta2 = float(input("dime el precio de la segunda venta: "))
venta3 = float(input("dime el precio de la tercera venta: "))

comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1

print("comision por ventas:",comision)
print("sueldo total:", sueldobase + comision)