cas= float(input("Zadej čas: "))

if cas < 0:
    input("Hodina nemůže být záporná.")
else: 
    if cas >= 24:
        print("Zadávejte platné hodiny.")

if cas <6:
    print("Dobrou noc")

if cas  <9:
    print("Dobré ráno")

if cas <12: 
    print("Dobré dopoledne")

if cas <17:
    print("Dobré odpoledne")

if cas <21:
    print("Dobrý večer")

if cas <23:
    print("Dobrou noc")
