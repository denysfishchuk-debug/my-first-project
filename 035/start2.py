

#  Безопасная запись в новый файл
print("Создание файла 'my_notes.txt' и запись строк через with...")
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("Строка 1: заметка через with.\n")
    file.write("Строка 2: ещё одна заметка.\n")
print("Файл успешно записан.\n")

# Добавление текста без перезаписи 
print("Добавление строк в 'my_notes.txt' через with...")
with open("my_notes.txt", "a", encoding="utf-8") as file:
    file.write("Строка 3: дополнение.\n")
    file.write("Строка 4: ещё одно дополнение.\n")
print("Строки успешно добавлены.\n")

# Чтение всего содержимого файла
print("Чтение всего содержимого файла через with:")
with open("my_notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Построчное чтение файла
print("Построчное чтение файла через with:")
with open("my_notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Обработка ошибки при открытии несуществующего файла
print("Попытка открыть несуществующий файл:")
try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Ошибка: файл 'missing_file.txt' не найден.")