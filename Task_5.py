# Работа с заметками. Задание 3
def build_note(note_text, note_name):
    # проверим существует ли файл с заданным названием, если нет то создаем новый,
    # если да - то заменим его нановую заметку
    try:
        file = open(f"{note_name}.txt", "r+", encoding = "utf-8")
    except IOError:
        file = open(f"{note_name}.txt", "w+", encoding = "utf-8")
    file.write(note_text)
    print(f"Заметка {note_name} создана.")

#Запрашивает у пользователя название и текст заметки, а затем вызывает функцию
def create_note():
    note_name = input('введите название файла с заметками: ')
    note_text = input('введите текст заметки: ')
    build_note(note_text, note_name)

#Запрашивает у пользователя название заметки если файл с таким названием
# существует, функция считывает содержимое файла и выводит его на экран.
# Если файла не существует, функция выводит сообщение, что заметка
# не найдена
def read_note():
    import os.path

    note_name_read = input('введите название файла с заметками: ')
    path = f"{note_name_read}.txt"
    if os.path.isfile(path):
        with open(f"{note_name_read}.txt", 'r') as file:
            lines = file.read()
        print('это сам текст данной заметки: ', lines)
    else:
        print('такая заметка не найдена')

#запрашивает у пользователя название заметки. Если файл с введенным
# именем существует, функция считывает и выводит содержимое файла,
# запрашивает у пользователя новый текст заметки и обновляет
# содержимое файла. Если файла не существует, она выводит сообщение,
# что заметка не найдена.
def edit_note():
    import os.path
    note_name_edit = input('введите название файла с заметками: ')
    path = f"{note_name_edit}.txt"
    if os.path.isfile(path):
        print('Такой файл с заметками уже существует! ')
        note_text_new = open(f"{note_name_edit}.txt", "w+")
        note_text_edit_new = input('Введите новую заметку в этот файл: ')
        note_text_new.write(note_text_edit_new)
        print(f"Новая заметка {note_name_edit} создана.")
    else:
        print('такая заметка не найдена')

#Она запрашивает у пользователя название заметки. Если файл с
# введенным именем существует, функция удаляет файл.
def delete_note():
    import os
    note_name_delete = input('введите название файла с заметками: ')
    path = f"{note_name_delete}.txt"
    if os.path.isfile(path):
        os.remove(f"{note_name_delete}.txt")
        print('Файл с заметками удален!')
    else:
        print('Такая заметка не найдена')

# вывод заметок в порядке по мере увеличению длины названия
def display_notes():
    import os
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    print(notes)
    sorted_notes = sorted(notes, key=len)
    print(sorted_notes)



def main():
    import colorama
    from colorama import Fore, Style

    # создадим бесконечный цикл работы с заметками
    while True:
        action = input('Меню выбора действий (нажмите определенную цифру для выбора последующих '
              'действий): ''\n''1 - для создания текстового файла с определенным названием '
              'и текстом заметки.''\n''2 - для вывода на экран содержимого заданной пользователем'
              ' заметки.''\n''3 - для вывода на экран содержимого запрашиваемой пользователем'
              ' заметки и ввода пользователем новой заметки.''\n''4 - для удаления указанной '
              'пользователем заметки.''\n''5 - для вывода упорядоченного по длине названия '
              'списка заметок.''\n''ваш выбор: ')
        if action == '1':
            create_note()
        if action == '2':
            read_note()
        if action == '3':
            edit_note()
        if action == '4':
            delete_note()
        if action == '5':
            display_notes()
        print(Fore.BLUE + 'для дальнейшего продолжения работы с заметками введите y/n' + Style.RESET_ALL)
        ans = input().lower()
        if ans == 'n':
            break
main()



