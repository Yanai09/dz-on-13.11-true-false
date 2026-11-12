kolichestvo = int(input())
predydushiy_hesh = 0
oshibka_blok = -1
for nomer in range(kolichestvo):
    blok = int(input())
    hesh = blok % 256
    sluchaynoe = (blok // 256) % 256
    dannye = blok // (256 ** 2)
    pravilnyy_hesh = (37 * (dannye + sluchaynoe + predydushiy_hesh)) % 256
    if hesh >= 100 or hesh != pravilnyy_hesh:
        if oshibka_blok == -1:
            oshibka_blok = nomer
    predydushiy_hesh = hesh
print(oshibka_blok)