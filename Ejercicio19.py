correct = int(input("dime las respuestas correctas: "))
incorrect = int(input("dime las respuestas incorrectas: "))
blanco = int(input("dime las respuestas en blanco: "))

nota = correct * 5 + incorrect * (-1) + blanco * 0
print("la nota final es:", nota)