summa = 0
d = 0
d1 = 0
while True:
    d += 1
    line  = int(input())
    summa += line
    if summa == 10:
        d1 = d
    elif line == 0:
       break
print(d1)
 