cat = False
st = 0
st1 = 0
while True:
    st += 1
    line  = str(input())
    if "кот" in line or "Кот" in line:
        cat = True
        st1 = st
    elif "СТОП" in line:
       break
if cat == True:
   print(st1)
else:
   print("-1")   