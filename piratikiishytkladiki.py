x = 0
y = 0 
x2 = int(input("Введите координату х:"))
y2 = int(input("Введите координату y:"))
shagi_kolvo = 0
nashli = (x == x2 and y == y2)
while True:
    napravlenie = input()
    if napravlenie == "стоп":
        break
    shagi = int(input())
if not nashli:
        if napravlenie == "север":
            y += shagi
        elif napravlenie == "юг":
            y -= shagi
        elif napravlenie == "восток":
            x += shagi
        elif napravlenie == "запад":
            x -= shagi
        shagi_kolvo += 1
        if x == x2 and y == y2:
            nashli = True
print(shagi_kolvo)