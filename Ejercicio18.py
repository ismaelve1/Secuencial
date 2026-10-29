nombre = input("dime tu nombre: ")
ape1 = input("dime tu primer apellido: ")
ape2 = input("dime tu segundo apellido: ")

inicial = nombre[0]
inicial = inicial + ape1[0]
inicial = inicial + ape2[0]
inicial = inicial.upper()
print("tus iniciales son:",inicial)