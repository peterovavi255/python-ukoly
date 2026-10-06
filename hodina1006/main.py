# polarita proměnné 

cislo = float(input("Zadej číslo: "))

if cislo >0:
    print("Kladné číslo")
else: 
    if cislo==0:
        print("Nula")
    else:
        print("Záporné")
        cislo= -cislo

print(f"Absolutní hodnota je {cislo}")
