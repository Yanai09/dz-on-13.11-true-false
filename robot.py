vchera = int(input())
kupleno = False
prodano = False
cena_pokupki = 0
cena_prodazhi = 0
while True:
    segodnya = int(input())
    if segodnya == 0:
        break
    if not kupleno and segodnya > vchera:
        cena_pokupki = segodnya
        kupleno = True
    elif kupleno and not prodano and segodnya < vchera:
        cena_prodazhi = segodnya
        prodano = True
    vchera = segodnya
vygoda = cena_prodazhi - cena_pokupki
print(cena_pokupki, cena_prodazhi, vygoda)