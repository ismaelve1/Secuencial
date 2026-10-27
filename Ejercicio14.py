num = int(input("dime un numero de dos cifras: "))
decenas = num // 10
unidades = num % 10

invertido = unidades * 10 + decenas

print("el numero invertido es:", invertido)