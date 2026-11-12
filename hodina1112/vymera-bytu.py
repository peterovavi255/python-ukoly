def obsah_obdelniku(a, b):

    if a <= 0 or b <= 0:
        return None
    obsah = a * b
    return obsah

print("Výpočet celkové výměry bytu.")
print("****************************")

pocet_mistnosti = int(input("Zadej počet místností: "))
mistnost1 = 1
celkova_vymera = 0

while mistnost1 <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost1} mistnosti.")
    strana_a = int(input("Zadej rozměr strany a v [m] "))
    strana_b = int(input("Zadej rozměr strany b v [m] "))
    obsah = obsah_obdelniku(strana_a, strana_b)

    if obsah != None:
        celkova_vymera += obsah
        mistnost1 += 1
    else: 
        print("Chybné zadání místnost!")
print(f"Celková výměra bytu je {celkova_vymera} m2.")