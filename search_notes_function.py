# Этап3_Финальное_Юнин_Константин.
# Задание 4: Функция поиска заметок

note_states = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '27-11-2024', 'issue_date': '30-11-2024'},

    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},

    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
                        ]   # Список словарей заметки
note_end = ("Имя пользователя: ", "Заголовок: ", "Описание: ",
            "Статус: ", "Дата создания: ", "Дедлайн: "
            )   # Список элементов заметки для вывода
spisok_slov = []    # Список ключевых слов для поиска по нескольким словам
search_ = []    # Список найденных по ключевым словам заметок
m = -1  # Индекс ключевого слова в списке search_ = []
data_ = 1


def search_notes(notes, keyword=None, status=None):
    dikt_ = []      # Список найденных по ключевым словам заметок
    keyword = keyword.lower() if keyword != None else keyword     # Проверка по критерию с любым регистром ввода
    status = status.lower() if status != None else status    # Проверка по критерию с любым регистром ввода
    if len(notes) == 0:  # Проверка на наличие заметок
        print("\033[32m" + "У вас нет сохранённых заметок.")
        return
    if keyword == None:     # Поиск по статусу
        for sub in notes:
            for val in sub.values():
                if status in val:
                    dikt_.append(sub)   # Добавление заметки с критерием в словарь
                    break
    elif status == None:    # Поиск по ключевому слову
        for sub in notes:
            for val in sub.values():
                if keyword in val.split():
                    dikt_.append(sub)   # Добавление заметки с критерием в словарь
                    break
    else:
        for sub in notes:       # Поиск по статусу и ключевому слову
            for val in sub.values():
                if keyword in val.split():
                    for val in sub.values():
                        if status in val:
                            dikt_.append(sub)   # Добавление заметки с критерием в словарь
                            break
                    break
    if len(dikt_) == 0 and spisok_slov == []:  # Проверка на наличие заметок, соответствующих критериям
        print("\033[32m" + "\nЗаметки, соответствующие запросу, не найдены.")
        return dikt_
    else:
        vivod_(dikt_)
        return dikt_

def proverka(stroka_):  # Проверка вводимых данных
    if stroka_ not in ["1", "2"]:  # Ввод отличается от 1 или 2
        print("Пожалуйста повторите ввод правильно: либо 1, либо 2!")
        return 0
    else:
        return int(stroka_)  # Возврат целого числа


def vivod_(notes):  # Вывод заметок в виде столбца
    if data_ == 1:
        for l, _dict_ in enumerate(notes):
            print('\033[32m' + 'Найдены заметки:')  # Изменение цвета текста на зелёный
            print("---------------")
            print('\033[32m' + 'Заметка №', (l+1), ':')  # Вывод номера заметки
            for i,res in enumerate(_dict_.keys()):
                print(f'{note_end[i]}'
                      f'{_dict_[res]}')


def vvod(stroka_):
    while True:
        if stroka_ in ["Введите ключевое слово: ","Нажмите Enter для продолжения" ]:
            vvod_ = input('\033[39m' + '\n' +
                  stroka_)  # Изменение цвета текста на стандартный
            return vvod_
        else:
            vvod_ = input(stroka_)
            vvod_ = proverka(vvod_)
            if vvod_ == 0:  # Проверка вводимых данных на ошибку
                continue
            else:
                return vvod_  # Возврат целого числа


# Программа
print("\nВвод данных, которые не соответствуют ни одной заметке.\n"
      "Ввод: search_notes(notes, keyword='Hello')")
search_ = search_notes(note_states, keyword='Hello')
vvod("Нажмите Enter для продолжения")
print("\nОбработка пустого списка заметок.\n")
search_ = search_notes({}, keyword='работы', status='выполнено')
vvod("Нажмите Enter для продолжения")
print("\nПоиск по ключевому слову. "
      "Ввод: search_notes(notes, keyword='покупок')\n")
search_ = search_notes(note_states, keyword='покупок')
vvod("Нажмите Enter для продолжения")
print("\nПоиск по статусу. "
      "Ввод: search_notes(notes, status='в процессе')\n")
search_ = search_notes(note_states, status='в процессе')
vvod("Нажмите Enter для продолжения")
print("\nПоиск по ключевому слову и статусу. "
      "Ввод: search_notes(notes, keyword='работы', status='выполнено')\n")
search_ = search_notes(note_states, keyword='работы', status='выполнено')
vvod("Нажмите Enter для продолжения")
print("\nПоиск по ключевому слову с нечувствительностью к регистру. "
      "Ввод: search_notes(notes, keyword='ПОКУПОК')\n")
search_ = search_notes(note_states, keyword='покупок')
vvod("Нажмите Enter для продолжения")
print("\nРеализация поиска по нескольким ключевым словам. "
      "Ввод: search_notes(notes, keyword='ПОКУПОК','работы')")
search_ = []
notes = note_states
data_ = 0
while True:
    if vvod("\nХотите ввести ключевое слово для поиска? 1Да/2Нет ") == 1:
        spisok_slov.append(vvod("Введите ключевое слово: "))
        continue
    else:
        print("\nБудет произведен поиск по введенным вами ключевым словам, принадлежащим одной заметке!")
        vvod("Нажмите Enter для продолжения")
        break
for m, ind_ in enumerate(spisok_slov):
    search_ = search_notes(notes, keyword=ind_)
    notes = search_ if len(search_) != 0 else notes
data_ = 1
vivod_(notes)