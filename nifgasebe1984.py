n = int(input("Введите количество команд: "))
enemy = "Евразия"
friend = "Остазия"
for i in range(n):
    command = input("Введите команду: ")
    if command == "С кем война?":
        print(enemy)
    elif command == "С кем мир?":
        print(friend)
    elif command == "Меняем":
        enemy, friend = friend, enemy