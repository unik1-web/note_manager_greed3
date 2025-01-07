# Задание: Работа с несколькими заметками
import re
from datetime import datetime

note_ = ("имя пользователя: ", "заголовок заметки: ", "описание заметки: ",
         "статус заметки (новая, в процессе, выполнено): ",
         "дату создания заметки: ", "дату истечения заметки (дедлайн): ")
note_end = ("Имя: ", "Заголовок: ", "Описание: ","Статус: ","Дата создания: ", "Дедлайн: ")
status_ = ("новая", "в процессе", "выполнено")
fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
         2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
         3: "Вы неправильно ввели статус заметки, повторите ввод!",
         4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно."}
ID = []
note = []
note_states = {}

def replace_dates(match_):      # Обработка любого ввода даты
    a = []
    b = 0
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}', '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}', '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y', '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d', '%Y:%m:%d', '%Y.%m.%d']
    for i, j in zip(c, d):                  # Проверка ввода на наличие в строке даты
        try:
            a = re.findall(i, match_)       # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
            b = datetime.strptime(a[0], j)  # Преобразование вырезанной строки в тип datetime
            b = datetime.date(b)            # Преобразование datetime в date
            return b                        # Выход из функции с аргументом date
        except:
            continue
    print(fraza[4])
    return 0                                # Выход из функции с аргументом 0, т.е. нужен повторный ввод даты

def proverka(stroka_, ind_):
    counter = 0                             # Счетчик заглавных букв
    if ind_ in [4, 5]:                      # Проверка на ввод даты и преобразование в тип datetime
        note[ind_] = replace_dates(note[ind_])
        if note[ind_] == 0: return 0        # Данные не прошли проверку. Выход из функции с аргументом 0
    elif ind_ == 3 and stroka_ not in status_: # Проверка на вхождение ввода в список статусов заметки
        print(fraza[3])
        return 0                            # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
    elif ind_ in [0, 1, 2]:
        for ch in stroka_:
            if ch.isupper(): counter += 1               # Проверка на заглавную букву
            if counter in [0] and ind_ in [0, 1, 2]:    # 0 заглавных букв
                print(fraza[counter])
                return 0                    # Выход из функции с аргументом 0, т.е. нужен повторный ввод

def vvod():
    c = -1                               # Индекс заметок пользователя
    lst = []                             # Копия списка ввода
    while True:                          # Ввод данных пользователем
        c += 1
        j = 0                            # Индекс заполнения списка для словаря заметок
        while True:
            if j == 6: break             # Выход при заполнении списка словаря заметок
            if j in [0,1,2]:             # Ввод данных пользователем
                note.append(input("Введите с Заглавной буквы " + note_[j]))
            else:
                note.append(input("Введите " + note_[j]))
            if proverka(note[j], j) == 0: # Введенные данные не прошли проверку
                note.pop(-1)              # Удаление из списка неправильно введенной строки
                continue
            j += 1
        lst = note.copy()                 # Копия списка ввода
        ID.append(id(c))
        note_states[ID[-1]] = lst          # Внесение данных в словарь с ключем ID
        if input("Хотите добавить ещё одну заметку? (да/нет):  ") not in ["да", "Y", "y"]:
            break                         # Проверка на необходимость ввода еще одной заметки
        else:
            c += 1
            note.clear()                  # Очистка списка ввода данных

print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
vvod()
# print(note_states)
print("Список заметок:")
# print(ID)
for i in range(len(ID)):        # Вывод списка заметок
    print(i+1,". ", end='')
    for j in range(6):
        if j in [0]:
            print("\t",note_end[j], note_states[ID[i]][j])
        else:
            print("\t\t",note_end[j], note_states[ID[i]][j])