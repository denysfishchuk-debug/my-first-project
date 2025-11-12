
# Создание нового файла и запись
print("Создание файла 'my_notes.txt' и запись строк...")
file = open("my_notes.txt", "w", encoding="utf-8")
file.write("Первая строка заметок.\n")
file.write("Вторая строка заметок.\n")
file.write("Третья строка заметок.\n")
file.close()
print("Файл успешно создан и закрыт.\n")

# Добавление текста к существующему файлу
print("Добавление новых строк в 'my_notes.txt'...")
file = open("my_notes.txt", "a", encoding="utf-8")
file.write("Добавленная строка 1.\n")
file.write("Добавленная строка 2.\n")
file.close()
print("Строки успешно добавлены.\n")

# Чтение всего содержимого файла
print("Чтение всего содержимого файла:")
file = open("my_notes.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# Построчное чтение файла
print("Построчное чтение файла:")
file = open("my_notes.txt", "r", encoding="utf-8")
for line in file:
    print(line.strip())  # удаляем лишние переносы
file.close()