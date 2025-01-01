# Цикл для добавления заголовков
# Инициализация списка с первым элементом " " и вспомогательных переменных
note = [" ",]
c = 0
s = "0"
# Цикл ввода данных в список, пока пользователь не остановит ввод, нажав только "Enter"
while len(note[c]) != 0:                    # Длина элемента списка не равна 0
    note.append(" ")                        # Добавление в список нового пустого элемента " "
    # Ввод данных пользователем в элемент списка
    note[c+1] = input("Введите один заголовок с заглавной буквы (или оставьте пустым для остановки): ")
    # Проверка заголовков на уникальность
    for el in range(len(note)):
        if note[c+1] == note[el] and c+1 != el:
            print("Вы ввели заголовок, который уже ввели ранее, поэтому повторите ввод заголовка заметки!")
            c = c - 1
            note.pop(-1)            
            break
    # Проверка на ввод заголовков без заглавной буквы и ввод нескольких заголовков
    counter = 0   
    for ch in note[c+1]:       
        if ch.isupper(): 
            counter += 1
        if counter == 0:
            print("Вы ввели заголовок без заглавной буквы, поэтому повторите ввод заголовка заметки! ")
            note.pop(c+1)
            c = c - 1
            break
        if counter == 2:
            print("Вы ввели несколько заголовков, поэтому повторите ввод заголовка заметки!")
            note.pop(c+1)
            c = c - 1
            break   
    c = c + 1                                  
# Выход из цикла при пустом поле ввода
print("Вы оставили поле ввода пустым, поэтому ввод заголовков прекращен!")
# Чистка списка от пустых строк
note.pop(0)
note.pop(c-1)
# Вывод на консоль введенных пользователем заголовков
print("\nЗаголовки заметки: ")
for idx in range(len(note)):                   # Цикл выполняется пока не выведет все элементы списка note
    print("-"+note[idx])
