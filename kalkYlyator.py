while True:
    pervoe_chislo = int(input())
    znak = input()
    if znak == "x":
        print(pervoe_chislo)
        break
    elif znak == "!":
        if pervoe_chislo >= 0:
            faktorial = 1
            for i in range(1, pervoe_chislo + 1):
                faktorial *= i
            print(faktorial)
    else:
        vtoroe_chislo = int(input())
        if znak == "+":
            print(pervoe_chislo + vtoroe_chislo)
        elif znak == "-":
            print(pervoe_chislo - vtoroe_chislo)
        elif znak == "*":
            print(pervoe_chislo * vtoroe_chislo)
        elif znak == "/":
            if vtoroe_chislo != 0:
                print(pervoe_chislo // vtoroe_chislo)
        elif znak == "%":
            if vtoroe_chislo != 0:
                print(pervoe_chislo % vtoroe_chislo)
