def draw_board(board):
    from colorama import Fore, Back, Style
    # запустить цикл, который проходит по всем элементам поля, проверяет их значение
    # и в зависимости от их значчений раскрашивает пустую ячейку в желтый цвет, 'X' в красный,
    # '0' в синий
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                A=Back.YELLOW
            elif board[i][j] == "X":
                A=Fore.RED
            else:
                A=Fore.BLUE
            print(A + board[i][j] + Style.RESET_ALL, "| ",end='')
            if j > 2:
                print(A + board[i][j] + Style.RESET_ALL, "| ")
        print("\n---------")

def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    # координаты x, y взять из функции ask_move(player, board)
    make_move(player, board, x, y)

def ask_move(player, board):
    # дать игроку возможность сделать ход, то есто есть ввести координаты
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y)
    # задать условие, которое проверяет, свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        # если клетка свободна, вернуть её координаты
        return (x, y)
    else:
        print("Клетка занята. Введите координаты еще раз.")
        return ask_move(player, board)

def make_move(player, board, x, y):
    # проверить, что клетка свободна
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    # если клетка свободна, записать ход
    board[x][y] = player
    return True

def check_win(player, board):
    # проверить, совпадают ли значения в строках и столбцах
    for i in range(3):
        # проверить, совпадают ли значения в строках
        if board[i] == [player, player, player]:
            return True
        # проверить, совпадают ли значения в столбцах
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # проверить, совпадают ли значения на диагонали из верхнего левого в нижний правый угол
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    # проверить, совпадают ли значения на диагонали из верхнего правого в нижний левый угол
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    # задать бесконечненый цикл, который проводит игры
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = "X"
        # задать бесконечнный цикл, который проводит конкретную игру
        while True:
            # нарисовать игровое поле
            draw_board(board)
            # запросить ход
            ask_and_make_move(player, board)
            # проверить, выиграл ли игрок
            if check_win(player, board):
                print(f"{player} выиграли!")
                break
            # проверить, произошла ли ничья
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == " ":
                        tie_game = True
            # если произошла ничья, завершить цикл
            if not tie_game:
                break
            player = "O" if player == "X" else "X"
        # спросить игроков, хотят ли они сыграть еще нраз
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != "y":
            break
tic_tac_toe()
print('final')