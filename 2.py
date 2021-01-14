with open('numere.txt', 'r') as f:
    a = f.readline()
    b = f.readline()
if int(a) > int(b):
    a = int(a) * 2
    b = int(b) * 3
elif int(b) > int(a):
    a = int(a) * 3
    b = int(b) * 2
else:
    a = b = 'Numerele sunt egale'
if a != b:
    with open('produs.txt', 'w') as f:
        f.write(str(a))
        f.write('\n')
        f.write(str(b)) 
else:
    with open('produs.txt', 'w') as f:
        f.write(str(a))