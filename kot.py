n = int(input())
cat = False
for i in range(n):
   line  = str(input())
   if "кот" in line or "Кот" in line:
      cat = True
if cat == True:
   print("МЯУ")
else:
   print("НЕТ")   