import math
num1 = float(input("dime un numero: "))

if num1 <= 0:
    print("el numero no puede ser negativo o 0")
else:
    cuadrada = math.sqrt(num1)
    print("la raiz cuadrada es: ", cuadrada)

    cubica = math.cbrt(num1)
    print("la raiz cubica es: ", cubica)