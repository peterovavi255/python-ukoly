cas = float(input("Zadej čas: "))

if cas < 0 :
    print("Zadávejte platné hodiny.")
elif cas >= 24:
    print("Zadávejte platné hodiny.")

elif cas < 6:
    print("Dobrou noc")
elif cas < 10:
    print("Dobré ráno")
elif cas < 13:
    print("Dobré dopoledne")
elif cas < 18:
    print("Dobré odpoledne")
elif cas < 22:
    print("Dobrý večer")
else:
    print("Dobrou noc")