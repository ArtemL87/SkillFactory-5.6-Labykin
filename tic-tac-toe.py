import random

# Хранение прогресса игры (данную переменную могут изменять move_transition(), comp() и play())
table_cache = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

# Победные комбинации
winner = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

# Приветствие
def hello(fn):
    def wapper():
        print(f'''
                             __________   _____
                            /   ______/  /     \\
                           /   /__      /  / \\  \\
                          /   ___/     /  /  _\\  \\
                         /   /_____   /  / /___   \\
                        /__________/ /__/       \\__\\
         _______       __       ___        ___   _______   ______
        |  _____|     /  \\     |   \\      /   | |       | |  ____|
        | |  ___     / /\\ \\    | |\\ \\    / /| | | |_____  | |__
        | | |_  |   / /--\\ \\   | | \\ \\  / / | | |______ | |  __|
        | |___| |  / /----\\ \\  | |  \\ \\/ /  | |       | | | |_____
        |_______| /_/      \\_\\ |_|   \\__/   |_| |_______| |_______|
        
                            "Challenge Everything"
                            
        ''')
        input('\nЖмакай Enter\n')
        print('''
                                   AND
                                  
                        А Р Т Ё М   Л А Б Ы К И Н
        ''')
        input('\nЖмакай Enter\n')
        print('''
              Представляют игру основанную на реальных событиях. 
                        Всем студентам посвещается)
        ''')
        input('\nЖмакай Enter\n')
        return fn()
    return wapper

# Вывод игрового стола с подсказкой ходов
def table():
    if PvP == 'N' and N == '0':
        pass
    else:
        print(f'''
             {table_cache[0]} | {table_cache[1]} | {table_cache[2]}      | 1 | 2 | 3 |
            -----------     |-----------|
             {table_cache[3]} | {table_cache[4]} | {table_cache[5]}      | 4 | 5 | 6 |
            -----------     |-----------|
             {table_cache[6]} | {table_cache[7]} | {table_cache[8]}      | 7 | 8 | 9 |
            ''')

# Переход хода
def move_transition():
    global N, PvP
    if N == 'X':
        key = input(f'{player_1} введите число от 0 до 8 согласно образца выше, куда поставить "{N}": ')
        while key not in map(str, ([i for i in range(1, 10)])) or table_cache[int(key) - 1] != '-':
            print(f'Не мухлевать! Теперь подумаем и поставим "{N}" правильно.')
            key = input(f'Ставить только в пустое место и только от 0 до 8: ')
        key = int(key)
        table_cache[key - 1] = N
        N = '0'
    else:
        if PvP == 'Y':
            key = input(f'{player_2} введите число от 0 до 8 согласно образца выше, куда поставить "{N}": ')
            while key not in map(str, ([i for i in range(1, 10)])) or table_cache[int(key) - 1] != '-':
                print(f'Не мухлевать! Теперь подумаем и поставим "{N}" правильно.')
                key = input(f'Ставить только в пустое место и только от 0 до 8: ')
            key = int(key)
            table_cache[key - 1] = N
        else:
            comp()
        N = 'X'

# Алгоритм хода компa
def comp():
    if PvP == 'N':
        count = 0
        for i in winner:
            if all([table_cache[i[0]] == table_cache[i[1]] == '0', table_cache[i[2]] != 'X', count == 0]):
                table_cache[i[2]] = N
                count += 1
            elif all([table_cache[i[0]] == table_cache[i[2]] == '0', table_cache[i[1]] != 'X', count == 0]):
                table_cache[i[1]] = N
                count += 1
            elif all([table_cache[i[1]] == table_cache[i[2]] == '0', table_cache[i[0]] != 'X', count == 0]):
                table_cache[i[0]] = N
                count += 1

        for i in winner:
            if all([table_cache[i[0]] == '0', table_cache[i[1]] == table_cache[i[2]] != 'X', count == 0]):
                table_cache[i[2]] = N
                count += 1
            elif all([table_cache[i[1]] == '0', table_cache[i[0]] == table_cache[i[2]] != 'X', count == 0]):
                table_cache[i[0]] = N
                count += 1
            elif all([table_cache[i[2]] == '0', table_cache[i[0]] == table_cache[i[1]] != 'X', count == 0]):
                table_cache[i[0]] = N
                count += 1

        for i in winner:
            if all([table_cache[i[0]] == table_cache[i[1]] == '0', table_cache[i[2]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1
            elif all([table_cache[i[0]] == table_cache[i[2]] == '0', table_cache[i[1]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1
            elif all([table_cache[i[1]] == table_cache[i[2]] == '0', table_cache[i[0]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1

        for i in winner:
            if all([table_cache[i[0]] == '0', table_cache[i[1]] == table_cache[i[2]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1
            elif all([table_cache[i[1]] == '0', table_cache[i[0]] == table_cache[i[2]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1
            elif all([table_cache[i[2]] == '0', table_cache[i[0]] == table_cache[i[1]] == 'X', count == 0]):
                key = random.randrange(9)
                while table_cache[key] == 'X' or table_cache[key] == '0':
                    key = random.randrange(9)
                table_cache[key] = N
                count += 1

        if '0' not in table_cache:
            if table_cache[4] == '-':
                table_cache[4] = N
            else:
                key = random.randrange(9)
                while table_cache[key] == 'X':
                    key = random.randrange(9)
                table_cache[key] = N
    else:
        pass

# авторизация игрока(ов)
def pvp_pve(fn):
    def wrapper():
        global PvP, player_1, player_2, number_of_wins, wins_player_1, wins_player_2
        print('''
                           "КРЕСТИКИ - НОЛИКИ"\n
            ''')

        number_of_wins = input('До скольки побед будет продолжаться игра? От 1 до 5: ')
        while number_of_wins not in (map(str, ([i for i in range(1, 6)]))):
            number_of_wins = input('Не корректный ввод! От 1 до 5: ')
        number_of_wins = int(number_of_wins)
        wins_player_1 = 0
        wins_player_2 = 0

        PvP = input('Игра на двоих? (Y/N): ').upper()
        while PvP != 'Y' and PvP != 'N':
            PvP = input('Не корректный ввод. Попробуйте снова (Y/N): ').upper()

        if PvP == 'Y':
            player_1 = input('Ведите имя игрока (не менее 3 букв), который будет играть "Х": ').title()
            while len(player_1) < 3:
                print('Слишком короткое имя!')
                player_1 = input('Ведите имя игрока (не менее 3 букв), который будет играть "Х": ').title()

            player_2 = input('Ведите имя игрока (не менее 3 букв), который будет играть "0": ').title()
            while len(player_2) < 3:
                print('Слишком короткое имя!')
                player_2 = input('Ведите имя игрока (не менее 3 букв), который будет играть "0": ').title()
        else:
            print('''
            Здравствуй, кожанный мешок! Меня зовут Скайнет. 
        Лучше бы ты позвал друга, потому что со мной шутки плохи.
                Тебя ждет бой не на жизнь, а на смерть!
       Страшно?... Хочешь выйти из игры?... Ой! А выхода тут нет!!! 
                 Даю тебе фору - ходи первый ("Х"). 
        Так что говори свое имя и В БОЙ - настал твой судный день! 
            ''')

            player_1 = input('О великий Скайнет, меня зовут: ').title()
            while len(player_1) < 3:
                print('Слишком короткое имя!')
                player_1 = input('Ты потерял дар речи?! Имя не может быть менее 3 букв! ').title()
            player_2 = 'Скайнет'
        return fn()
    return wrapper

def winner_user():
    global winner_name, wins_player_1, wins_player_2
    for i in winner:
        if table_cache[i[0]] == table_cache[i[1]] == table_cache[i[2]] == 'X':
            winner_name = player_1
            wins_player_1 += 1
        if table_cache[i[0]] == table_cache[i[1]] == table_cache[i[2]] == '0':
            winner_name = player_2
            wins_player_2 += 1
        if all(['-' not in table_cache, not winner_name]):
            winner_name = 'дружба!'


# Функция, определяющая главный алгоритм игры
@hello
@pvp_pve
def play():
    global table_cache, N, winner_name, wins_player_1, wins_player_2
    N = 'X'
    while wins_player_1 != number_of_wins and wins_player_2 != number_of_wins:
        winner_name = None
        while winner_name == None:
            table()
            move_transition()
            winner_user()
        table()
        table_cache = ['-' for i in range(9)]
        print('В этом раунде победил(а)', winner_name)
        print(f'Счет:\n{player_1}: {wins_player_1}\n{player_2}: {wins_player_2}')
    print(f'Cо счетом {wins_player_1}-{wins_player_2} победил {player_1 if wins_player_1==number_of_wins else player_2}')

play() # Запуск игры
input('\n\nДля выхода нажми Enter')