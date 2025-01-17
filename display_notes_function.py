# Этап3_Финальное_Юнин_Константин.
# Задание 3: Функция отображения заметок

from datetime import datetime
from tabulate import tabulate

note_states = [
    {'username': 'Алексей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '25-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '03-12-2024', 'issue_date': '11-12-2024'},
    {'username': 'Иван', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '19-11-2024', 'issue_date': '26-11-2024'},
    {'username': 'Андрей', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '24-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Анна', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '02-12-2024', 'issue_date': '11-12-2024'},
    {'username': 'Ираида', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '23-11-2024', 'issue_date': '26-11-2024'},
    {'username': 'Акакий', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '20-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Артур', 'title': 'План учёбы и работы',
     'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '01-12-2024', 'issue_date': '11-12-2024'},
    {'username': 'Эльза', 'title': 'План работы',
     'content': 'План работы', 'status': 'выполнено',
     'created_date': '22-11-2024', 'issue_date': '26-11-2024'},
    {'username': 'Гомер', 'title': 'Список покупок',
    'content': 'Купить продукты на неделю', 'status': 'новая',
    'created_date': '21-11-2024', 'issue_date': '30-11-2024'}
]       # Список словарей заметки
phrase = {
    0: "Какой вывод заметок предпочитаете? (1Заголовки/2Полные данные) ",
    1: "Сортировать заметки по дате? (1Да/2Нет) ",
    2: "Какой вывод заметок предпочитаете? (1Построчный/2Табличный) ",
    3: "Cортировать заметки по дате создания или дедлайну? 1/2: ",
    4: "Нажмите Enter для продолжения"
}             # Словарь фраз для вывода
note_end = (
    "Имя пользователя: ", "Заголовок: ",
    "Описание: ", "Статус: ",
    "Дата создания: ", "Дедлайн: "
)           # Список элементов заметки для вывода
note_keys = (
    "username", "title", "content", "status",
    "created_date", "issue_date"
)          # Кортеж ключей словаря заметки


def display_notes(notes):
    global data_
    if len(notes) == 0:     # Проверка на наличие заметок
        print("У вас нет сохранённых заметок.")
        return
    data_ = data_entry(phrase[0])
    if data_entry(phrase[1]) == 1:
        notes = sorting_(notes)     # Сортировка списка словарей по дате создания или дедлайну
    if data_ == 2:
        if data_entry(phrase[2]) == 2:
            output_tab(notes)       # Вывод заметок в виде таблицы
            return
    output_(notes)          # Вывод заметок построчно


def data_entry(string_):
    while True:
        if string_ == phrase[4]:
            input('\033[39m' +
                  string_)          # Изменение цвета текста на стандартный
            return
        else:
            date_ = input(string_)
            date_ = check_(date_)
            if date_ == 0:          # Проверка вводимых данных на ошибку
                continue
            else:
                return date_        # Возврат целого числа


def check_(string_):        # Проверка вводимых данных
    if string_ not in ["1", "2"]:       # Ввод отличается от 1 или 2
        print("Пожалуйста повторите ввод правильно: 1, либо 2!")
        return 0
    else:
        return int(string_)         # Возврат целого числа


def sorting_(notes):
    if data_entry(phrase[3]) == 1:      # Сортировка словаря по дате создания или дедлайну
        notes.sort(key=lambda x: datetime.strptime(x['created_date'], '%d-%m-%Y'))
    else:
        notes.sort(key=lambda x: datetime.strptime(x['issue_date'], '%d-%m-%Y'))
    return notes        # Возврат отсортированного списка словарей


def output_(notes):         # Вывод заметок в виде столбца
    print('\033[32m' + 'Список заметок:')       # Изменение цвета текста на зелёный
    print("---------------")
    for l, _dict_ in enumerate(notes):
        if data_ == 2:
            if (l % 5) == 0 and l != 0:
                data_entry(phrase[4])
            print('\033[32m' + 'Заметка №', (l+1), ':')         # Вывод номера заметки
            for i, res in enumerate(_dict_.keys()):
                print(
                      f'{note_end[i]}'
                      f'{_dict_[res]}'
                )       # Вывод заметок по образцу
        else:
            print('\033[32m' + 'Заметка №', (l + 1), ':')       # Вывод номера заметки
            print(
                f'{note_end[1]}'        # Вывод заголовков построчно
                f'{notes[l][note_keys[1]]}'
            )
        print("---------------------")


def output_tab(notes):          # Вывод заметок в виде таблицы
    print('\033[32m' + 'Список заметок:\n')
    print(tabulate(notes, headers='keys'))
    print('\033[39m')
    return


# Программа
display_notes(note_states)
print('\033[39m')       # Изменение цвета текста на стандартный
