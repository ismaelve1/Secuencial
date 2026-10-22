parcial1 = float(input("dime la primera nota parcial: "))
parcial2 = float(input("dime la segunda nota parcial: "))
parcial3 = float(input("dime la tercera nota parcial: "))

examen = float(input("dime la nota del examen final: "))
trabajo = float(input("dime la nota del trabajo final: "))

mediaparcs = (parcial1 + parcial2 + parcial3) / 3

notafin = (mediaparcs * 0.55) + (examen * 0.30) + (trabajo * 0.15)

print("tu nota final es:", round(notafin, 2))

