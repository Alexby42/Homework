from tkinter import *
import random

'''Объявление переменных'''
root = Tk()
root.title('Tic-Tac-Toe')
game_run = True
field = []
count = 0

'''Обработка нажатия кнопок'''
def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'turquoise'
    global game_run
    game_run = True
    global count
    count = 0
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global count
        count += 1
        check_win('X')
        if game_run and count < 5:
            computer_step()
            check_win('O')

'''Проверка победы'''
def check_win(sbl):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], sbl)
        check_line(field[0][n], field[1][n], field[2][n], sbl)
    check_line(field[0][0], field[1][1], field[2][2], sbl)
    check_line(field[2][0], field[1][1], field[0][2], sbl)

def check_line(a1, a2, a3, sbl):
    if a1['text'] == sbl and a2['text'] == sbl and a3['text'] == sbl:
        a1['background'] = a2['background'] = a3['background'] = 'purple'
        global game_run
        game_run = False

'''Действия компьютера'''
def can_win(a1, a2, a3, sbl):
    res = False
    if a1['text'] == sbl and a2['text'] == sbl and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == sbl and a2['text'] == ' ' and a3['text'] == sbl:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == sbl and a3['text'] == sbl:
        a1['text'] = 'O'
        res = True
    return res

def computer_step():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

'''Графика'''
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, font=('Lucida Console', 30, 'bold'), background='turquoise',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='ew')
root.mainloop()