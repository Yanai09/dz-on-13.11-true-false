cat = False
st = 0
st1 = 0
st2 = 0
while True:
    st += 1
    line  = str(input())
    if "кот" in line or "Кот" in line:
        cat = True
        st1 = st
        st2 = st
    elif "СТОП" in line:
       break
if cat == True:
   print(st2, st1)
else:
   print("0 -1")   