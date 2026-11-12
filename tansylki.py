terpenie = int(input())
oshibki = 0
pravilno = 0
nomer_scheta = 1

while oshibki < terpenie:
    slovo = input()
    
    if nomer_scheta == 1:
        nuzhnoe_slovo = "раз"
    elif nomer_scheta == 2:
        nuzhnoe_slovo = "два"
    elif nomer_scheta == 3:
        nuzhnoe_slovo = "три"
    else:
        nuzhnoe_slovo = "четыре"
        
    if slovo == nuzhnoe_slovo:
        pravilno += 1
        nomer_scheta += 1
        if nomer_scheta > 4:
            nomer_scheta = 1
    else:
        print(f"Правильных отсчётов было {pravilno}, но теперь вы ошиблись.")
        oshibki += 1
        pravilno = 0
        nomer_scheta = 1

print("На сегодня хватит.")
