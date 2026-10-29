m2 = int(input("monedas de 2 euros: "))
m1 = int(input("monedas de 1 euro: "))
m50 = int(input("monedas de 50 centimos: "))
m20 = int(input("monedas de 20 centimos: "))
m10 = int(input("monedas de 10 centimos: "))

total_cents = m2 * 200 + m1 * 100 + m50 * 50 + m20 * 20 + m10 * 10

euros = total_cents // 100
cents = total_cents % 100

print("tenemos", euros, "euros y", cents, "centimos")