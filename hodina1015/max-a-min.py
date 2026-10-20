a = 15
b = 42
c = 7

min= a
max= a

if b< min:
    min= b
elif b> max:
    max= b

if c< min:
    min= c
elif c> max:
    max= c

print("Minimum je:", min)
print("Maximum je:", max)