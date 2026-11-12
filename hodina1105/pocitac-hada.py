print("Mysli si celé číslo od 1 - 100.")

dole = 1
nahore = 100
pokusy = 0
odpoved = "" 

while odpoved != "s":
    pokusy += 1
    tip = (dole + nahore) // 2
    odpoved = input(f"Můj tip č. {pokusy} je {tip}. Je to správně (s), větší (v) nebo menší (m)? ")
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
else: 
    odpoved == "s"
    print(f"Tvé číslo bylo {tip}, uhádl jsem za {pokusy} pokusů.")