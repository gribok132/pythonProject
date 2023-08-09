def is_game_over(): # Функция для проверки идет ли еще игра.
    for row in game_map:
        if '-' in row:
            return True


def check_victory(win_check_map):  # Все выигрышные варианты каждой из сторон.
    if (win_check_map[1][1] == "x" and win_check_map[1][2] == "x" and win_check_map[1][3] == "x") or \
            (win_check_map[2][1] == "x" and win_check_map[2][2] == "x" and win_check_map[2][3] == "x") or \
            (win_check_map[3][1] == "x" and win_check_map[3][2] == "x" and win_check_map[3][3] == "x") or \
            (win_check_map[1][1] == "x" and win_check_map[2][1] == "x" and win_check_map[3][1] == "x") or \
            (win_check_map[1][2] == "x" and win_check_map[2][2] == "x" and win_check_map[3][2] == "x") or \
            (win_check_map[1][3] == "x" and win_check_map[2][3] == "x" and win_check_map[3][3] == "x") or \
            (win_check_map[1][1] == "x" and win_check_map[2][2] == "x" and win_check_map[3][3] == "x") or \
            (win_check_map[1][3] == "x" and win_check_map[2][2] == "x" and win_check_map[3][1] == "x"):
        print("Игрок с символом х - победил")
        exit()
    elif (win_check_map[1][1] == "o" and win_check_map[1][2] == "o" and win_check_map[1][3] == "o") or \
            (win_check_map[2][1] == "o" and win_check_map[2][2] == "o" and win_check_map[2][3] == "o") or \
            (win_check_map[3][1] == "o" and win_check_map[3][2] == "o" and win_check_map[3][3] == "o") or \
            (win_check_map[1][1] == "o" and win_check_map[2][1] == "o" and win_check_map[3][1] == "o") or \
            (win_check_map[1][2] == "o" and win_check_map[2][2] == "o" and win_check_map[3][2] == "o") or \
            (win_check_map[1][3] == "o" and win_check_map[2][3] == "o" and win_check_map[3][3] == "o") or \
            (win_check_map[1][1] == "o" and win_check_map[2][2] == "o" and win_check_map[3][3] == "o") or \
            (win_check_map[1][3] == "o" and win_check_map[2][2] == "o" and win_check_map[3][1] == "o"):
        print("Игрок с символом o - победил")
        exit()


def over(): # Функция завершения, когда все клетки заполнены.
    print("\nИгра окончена ничьей с результатом:\n")
    for char in range(4):
        print(*game_map[char])


game_map = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]
for i in range(4):
    print(*game_map[i])


def game_coordinate(): # Узнаем координаты для символа
    coord_x = input("Введите номер строки: ")
    coord_y = input("Введите номер столбца: ")
    coord_list = [coord_x, coord_y]
    return coord_list


def game(): # Основное тело функции.
    while is_game_over() and not check_victory(game_map):
        list_ = game_coordinate()
        x, y = list_[0], list_[1]
        if not (x.isdigit()) or not (y.isdigit()):
            print("\nВведите число\n")
            continue
        if (0 < int(x) <= 3) and (0 < int(y) <= 3):
            char = str(input("Введите символ x или o: "))
            if game_map[int(x)][int(y)] != '-':
                print("\nЭта клетка уже занята")
            elif char == 'x' or char == 'o':
                game_map[int(x)][int(y)] = char
                for char_ in range(4):
                    print(*game_map[char_])
            else:
                print(f"\nВвод {char} некорректен\n")
        else:
            print("\nНеверные координаты\n")

    over()


game()
