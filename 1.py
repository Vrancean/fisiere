  with open('numere.txt', 'r') as f:
    a = f.readline()
    b = f.readline()
if int(a) > int(b):
    x = int(b)
if int(a) < int(b):
    x = int(a)
else:
    x = 'Numerele sunt egale'
with open('minim.txt', 'w') as f:
    f.write(str(x))
