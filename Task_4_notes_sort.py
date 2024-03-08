# Задание 4
# вывод заметок в порядке по мере увеличению длины названия
def display_notes():
    import os
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    print(notes)
    sorted_notes = sorted(notes, key=len)
    print(sorted_notes)

display_notes()



