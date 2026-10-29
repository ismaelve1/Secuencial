hh = int(input("hora de salida: "))
mm = int(input("minutos de salida: "))
ss = int(input("segundos de salida: "))
t = int(input("tiempo de viaje en segundos: "))

salida = hh * 3600 + mm * 60 + ss
llegada = salida + t

llegada = llegada % 86400

horas = llegada // 3600
minutos = (llegada % 3600) // 60
segundos = llegada % 60

print(f"La hora de llegada es: {horas:02d}:{minutos:02d}:{segundos:02d}")