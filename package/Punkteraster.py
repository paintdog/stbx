

# Punkteraster berechnen

gesamtpunktzahl = 80
prozente = [100 - i for i in range(5, 100, 5) if i <= 75]

print('Punkteraster bei maximal {} Gesamtpunkten\n'.format(prozente))


letzter_wert = gesamtpunktzahl

for stufe in prozente:

    neuer_wert = int(gesamtpunktzahl * stufe / 100)

    print("{}-{}".format(letzter_wert, neuer_wert), end=",")

    letzter_wert = neuer_wert - 1

print("{}-{}".format(letzter_wert - 1, 0))


