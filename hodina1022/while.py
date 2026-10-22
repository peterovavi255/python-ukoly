vek = int(input("Zadej věk: "))
if vek<18:
    print("Jsi nezletilý")

vek = int(input("Zadej věk: "))
while vek<18 and vek>=0:
    print("Jsi nezletilý")
    vek = int(input("Opakuj zadání: "))
if (vek>=18):
    print("Přístup povolen")
else:
    print("Přístup není povolen")