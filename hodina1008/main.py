# souřadnice objektu
x_panacka=int(input("Zadej souřadnici X: "))
y_panacka=int(input("Zadej souřadnici Y: "))

# souřadnice "nebezpečné" oblasti (kolizní oblast)
x1 = 2
x2 = 6
y1 = 2
y2 = 5

# test, zda došlo ke kolizi
if x_panacka>=x1 and x_panacka<=x2 and y_panacka>=y1 and y_panacka<=y2:
    print("Došlo ke kolizi!")
else: 
    print("Objekt mimo kolizní zónu..")
