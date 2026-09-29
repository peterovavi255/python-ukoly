#************************
# Kalkulačka spropitného
#29.9.2026
#************************

print("Vítejte v kalkulačce spropitného!")
celkova_castatka = float(input("Zadejte celkovou částku účtu: "))
spropitne = int(input("Zadejte spropitné v procentech: "))
pocet_osob = int(input("Zadejte počet osob u stolu: "))

spropitne_Kc = celkova_castatka * (spropitne / 100)
celkova_castatka += spropitne_Kc

zaplacena_castatka = round(celkova_castatka / pocet_osob, 2)
print(f"Zaplatíš 1/{pocet_osob} z {celkova_castatka} Kč ({zaplacena_castatka} Kč)")
