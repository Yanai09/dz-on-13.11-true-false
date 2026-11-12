storona = float(input())
skorost = float(input())
povoroty = 0
while storona > skorost and abs(storona - skorost) > 0.01:
    storona = ((storona - skorost) ** 2 + skorost ** 2) ** 0.5
    povoroty += 1
print(povoroty)