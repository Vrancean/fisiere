with open("globulete.txt",'r')as f:
    a=f.readline()
b=3*int(a)
c=int(a)+b-2
t=int(a)+b+c
with open("bradut.txt", 'w') as f:
    f.write(str(t))