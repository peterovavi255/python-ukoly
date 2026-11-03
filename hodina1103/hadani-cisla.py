import random
tajne_cislo = random.randint(1,20)
pocitadlo = 0
tip = 0
max_pokusu = 5

print(f"Hádej číslo od 1 do 20. Máš {max_pokusu} pokusů.")

while tip!= tajne_cislo and pocitadlo <= max_pokusu:
    tip = int(input("Zadej svůj tip: "))
    if tip >= 1 and tip <= 20:
        pocitadlo += 1
        if tip > tajne_cislo:
            print("Moje číslo je menší.")
        elif tip < tajne_cislo:
            print("Moje číslo je větší.")
    else:
        print("Zadal jsi číslo mimo rozsah (1–20)!")

if tip == tajne_cislo:
    print(f"Úhádl jsi číslo {tajne_cislo} za {pocitadlo} pokusů.")
else:
    print(f"Překračil jsi {max_pokusu} pokusů. Číslo bylo {tajne_cislo}.")