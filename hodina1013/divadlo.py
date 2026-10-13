pocet=int(input("Zadej počet osob: "))
vek=float(input("Zadej věk osob: "))
student=input("Student [ano/ne]: ")

cena_zaklad = 500
nazev_slevy = ""

if pocet>=4:
    cena_celkem = pocet * cena_zaklad * 0.75
    nazev_slevy = "Skupinová sleva"
else:
    if vek<26 and student=="ano":
        cena_celkem = pocet * cena_zaklad * 0.7
        nazev_slevy = "Studentská sleva"
    elif vek>=65:
        cena_celkem = pocet * cena_zaklad * 0.8
        nazev_slevy = "Sleva pro seniory"
    else: 
        cena_celkem = pocet * cena_zaklad

print("Celková cena: ",cena_celkem, "Kč")
print("Cena jedné vstupenky: ",cena_celkem/pocet, "Kč")
if nazev_slevy!="":
    print(nazev_slevy)
