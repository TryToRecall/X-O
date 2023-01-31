field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def field_check():
    print(f"  0  1  2")
    for i in range(3):
        print(f"{i} {field[i][0]}  {field[i][1]}  {field[i][2]}")


def ur_turn():
    while True:
        cords = input("Твой ход: ").split()

        if len(cords) != 2:
            print("Введите две координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вы убежали за пределы поля!")
            continue

        if field[x][y] != " ":
            print("Выберите другую клетку")
            continue

        return x, y


def win_check():
    for i in range(3):
        checklist = []
        for j in range(3):
            checklist.append(field[i][j])
        if checklist == ['X', 'X', 'X'] or checklist == ['0', '0', '0']:
            print(f'Игра окончена, победа достаётся {(field[i][j])}!')
            return True

    for i in range(3):
        checklist = []
        for j in range(3):
            checklist.append(field[j][i])
        if checklist == ['X', 'X', 'X'] or checklist == ['0', '0', '0']:
            print(f'Игра окончена, победа достаётся {(field[j][i])}!')
            return True

    checklist = []
    for i in range(3):
        checklist.append(field[i][i])
    if checklist == ['X', 'X', 'X'] or checklist == ['0', '0', '0']:
        print(f'Игра окончена, победа достаётся {(field[i][i])}!')
        return True

    checklist = []
    for i in range(3):
        checklist.append(field[i][2 - i])
    if checklist == ['X', 'X', 'X'] or checklist == ['0', '0', '0']:
        print(f'Игра окончена, победа достаётся {(field[i][i])}!')
        return True

    return False


def greeting():
    print('________________________')
    print('    Добро пожаловать')
    print('в игру "Крестики-нолики"')
    print('________________________')
    print('Правила ввода ходов:')
    print('формат ввода -  x и y')
    print('x - номер строки')
    print('y - номер столбца')


greeting()

for i in range(10):

    field_check()
    if i == 9:
        print("Ничья!")
        break
    elif i == 0:
        print("Да начнётся битва! Крестоносцы, ваш ход!")
    elif i % 2 == 0:
        print("Ход крестиков")
    else:
        print('Ход ноликов')

    x, y = ur_turn()

    if i == 0:
        field[x][y] = "X"
    elif i % 2 == 0:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_check():
        break
