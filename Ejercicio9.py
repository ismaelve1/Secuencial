precio1 = float(input("dime el precio de tu compra "))

condescuento = precio1 * 0.15
total = precio1 - condescuento

print("el descuento es de:", round(condescuento, 2), "euros")
print("el total a pagar es de:", round(total, 2), "euros")