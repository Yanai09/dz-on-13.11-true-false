n = int(input())
cat = False
for i in range(n):
   line  = str(input())
   if "кот" in line or "Кот" in line:
      cat = True
   elif "пёс" in line or "Пёс" in line:
       cat = False
if cat == True:
   print("МЯУ")
else:
   print("НЕТ")