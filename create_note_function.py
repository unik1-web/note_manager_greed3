# Этап2_Финальное_Юнин_Константин.
# Задание: Работа с несколькими заметками
import re
from datetime import date, datetime



def create_note():
    global ID, note_, note_states
    note_ = ("имя пользователя: ",
             "заголовок заметки: ",
             "описание заметки: ",
             "статус заметки (новая, в процессе, выполнено): ",
             "дату дедлайна (день-месяц-год):")        # Список элементов заметки для ввода
    note_end = ("Имя: ", "Заголовок: ",
                "Описание: ","Статус: ",
                "Дата создания: ", "Дедлайн: ")     # Список элементов заметки для вывода
    status_ = ("новая", "в процессе",
               "выполнено")      # Список статусов заметки для ввода
    fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
             1: "Вы ввели заголовок, который уже вводили ранее, поэтому повторите ввод заголовка заметки!",
             2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
             3: "Вы неправильно ввели статус заметки, повторите ввод!",
             4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
             5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!"}        # Словарь фраз для вывода
    note_states = {"username": "", "title": "",
                   "content": "", "status": "",
                   "created_date": "",
                   "issue_date": ""}  # Список словарей заметки
    # vivod_tab = ("\t", "\t\t", "\t\t", "\t\t",
    #              "\t\t", "\t\t")  # Список табуляции элементов заметки для вывода
    # ID = []  # Ключ ID для уникальности каждой заметки
    note = []  # Список данных текущей заметки
    error = 0  # Счетчик ошибок



    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    print("Вводите строки с заглавной буквы, а даты в любом числовом формате (10-10-2024 и т.п.):")
    # e = -1  # Индекс заметок пользователя
    # lst = []  # Копия списка ввода
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while True:  # Ввод данных пользователем
        # e += 1
        # ind_ = 0  # Индекс заполнения списка для словаря заметок
        if ind_ == 5: break  # Выход при заполнении списка словаря заметок
        stroka_ = input("Введите " + note_[ind_])  # Ввод данных пользователем
        while True:
            error = 0
            # if ind_ == 5: break  # Выход при заполнении списка словаря заметок
            # stroka_ = input("Введите " + note_[ind_]) # Ввод данных пользователем
            #Проверка
            counter = 0  # Счетчик заглавных букв
            # if ind_ in [4] and stroka_ == "":  # Пустой ввод даты создания заметки
            #     note[ind_] = date.today()  # Присвоение дате создания заметки текущей даты
            #     return
            if ind_ in [5]:
                # Проверка даты дедлайна
                a = []  # Список вхождений даты в строке
                b = 0  # Временная переменная преобразования даты
                c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
                     '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
                     '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
                     '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']  # Список шаблонов даты
                d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
                     '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
                     '%Y:%m:%d', '%Y.%m.%d']  # Список форматов вывода даты
                for i, j in zip(c, d):  # Проверка ввода на наличие в строке даты
                    try:
                        a = re.findall(i, stroka_)  # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
                        b = datetime.strptime(a[0], j)  # Преобразование вырезанной строки в тип datetime
                        b = datetime.date(b)  # Преобразование datetime в date
                        break # Выход  с аргументом date
                    except:
                        continue
                print(b, type(b))
                if type(b) != datetime:
                    print(fraza[4])  # Вывод предупреждения об ошибке
                    continue
                # else: break
            #         error = 1  # Переменная ошибки 0  , т.е. нужен повторный ввод даты
            # if error == 1: continue  # Повторный ввод даты


                # note[j] = replace_dates(note[ind_])  # Проверка на ввод даты и преобразование в тип datetime
                # if note[ind_] == 0: return 0  # Данные не прошли проверку. Выход из функции с аргументом 0
                if (note[ind_] - date.today()).days <= 0:  # Дата создания меньше или равна даты дедлайна
                    print(fraza[5])
                    continue  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
            elif ind_ == 3 and stroka_ not in status_:  # Проверка на вхождение ввода в список статусов заметки
                print(fraza[3])
                continue  # Выход из функции с аргументом 0, т.е. нужен повторный ввод статуса
            elif ind_ in [0, 1, 2]:  # Проверка на ввод имени заметки, заголовка и описания
                for ch in stroka_:
                    if ch.isupper(): counter += 1  # Проверка на заглавную букву
                    if (counter in [0] and ind_ in
                            [0, 1, 2]):  # 0 заглавных букв - ошибка
                        print(fraza[0])
                        error = 1
                        break  # Выход из функции с аргументом 0, т.е. нужен повторный ввод
                if error == 1: continue  # Повторный ввод
                # for i in range(e - 1):
                #     if stroka_ == note_states[ID[i]][1]:  # Проверка заголовка заметки на уникальность
                #         print(fraza[1])
                #         error = 1
                #         continue  # Выход из функции с аргументом 0, т.е. нужен повторный ввод

            # if proverka(note[j], j) == 0:  # Введенные данные не прошли проверку
            #     note.pop(-1)  # Удаление из списка неправильно введенной строки
            #     continue
            note[ind_] = stroka_
            ind_ += 1

# Программа "Менеджер заметок"

# vvod()
print("Список заметок:")
# vivod()
create_note()
