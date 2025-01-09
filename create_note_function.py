# Этап3_Финальное_Юнин_Константин.
# Задание1: Работа с несколькими заметками
import re
from datetime import date, datetime


def create_note():    
    note_ = ("имя пользователя: ",
             "заголовок заметки: ",
             "описание заметки: ",
             "статус заметки (новая, в процессе, выполнено): ",
             "дату дедлайна (день-месяц-год):")        # Список элементов заметки для ввода
    status_ = ("новая", "в процессе",
               "выполнено")      # Список статусов заметки для ввода
    fraza = {0: "Вы ввели текст без заглавной буквы, поэтому повторите ввод!",
             1: "Вы ввели заголовок, который уже вводили ранее, поэтому повторите ввод заголовка заметки!",
             2: "Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!",
             3: "Вы неправильно ввели статус заметки, повторите ввод!",
             4: "Неверный формат даты. Пожалуйста, убедитесь, что дата введена правильно.",
             5: "Дата дедлайна не может быть раньше даты создания заметки, повторите ввод!"}        # Словарь фраз для вывода
    note_keys = ("username", "title", "content", 
                   "status", "created_date", "issue_date")  # Список ключей словаря заметки
    note_states = {}    # Словарь заметки
    c = ['\\d{2}/\\d{2}/\\d{2,4}', '\\d{2}-\\d{2}-\\d{2,4}',
         '\\d{2}:\\d{2}:\\d{2,4}', '\\d{2}.\\d{2}.\\d{2,4}',
         '\\d{2,4}/\\d{2}/\\d{2}', '\\d{2,4}-\\d{2}-\\d{2}',
         '\\d{2,4}:\\d{2}:\\d{2}', '\\d{2,4}.\\d{2}.\\d{2}']  # Список шаблонов даты
    d = ['%d/%m/%Y', '%d-%m-%Y', '%d:%m:%Y',
         '%d.%m.%Y', '%Y/%m/%d', '%Y-%m-%d',
          '%Y:%m:%d', '%Y.%m.%d']  # Список форматов вывода даты
    note = []  # Список данных текущей заметки    

    print('Добро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    print("Вводите строки с заглавной буквы, а даты в любом числовом формате (10-10-2024 и т.п.):")
    ind_ = 0  # Индекс заполнения списка для словаря заметок
    while True:  # Ввод данных пользователем
        if ind_ == 5: break  # Выход при заполнении списка словаря заметок
        stroka_ = input("Введите " + note_[ind_])  # Ввод данных пользователем
        error = 0   # Счетчик ошибок
        counter = 0  # Счетчик заглавных букв
        if ind_ in [4]:                # Проверка даты дедлайна
            a = [] # Список вхождений даты в строке
            b = 0  # Временная переменная преобразования даты            
            for i, j in zip(c, d):  # Проверка ввода на наличие в строке даты
                try:
                    a = re.findall(i, stroka_)  # Поиск в строке ввода даты по имеющимся в списке [c] шаблонам
                    b = datetime.strptime(a[0], j)  # Преобразование вырезанной строки в тип datetime
                    b = datetime.date(b)  # Преобразование datetime в date
                    break # Выход  с аргументом date
                except:
                    continue
            if str(type(b)) != "<class 'datetime.date'>":
                print(fraza[4])  # Вывод предупреждения об ошибке
                continue
            if (b - date.today()).days <= 0:  # Дата создания меньше или равна даты дедлайна
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
        if ind_ == 4:
            note.append(str(date.today().strftime("%d.%m.%Y")))
            note.append(str(b.strftime("%d.%m.%Y")))
        else:
            note.append(stroka_) 
        ind_ += 1
    i=0
    for t in note_keys:
        note_states[t] = note[i]
        i += 1
    print("Заметка создана:", note_states)

# Программа "Менеджер заметок"
create_note()