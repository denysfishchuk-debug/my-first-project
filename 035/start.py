try:
    print("10 / 0 =", 10 / 0)  # ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError: деление на ноль невозможно.")


# TypeError
try:
    len(42)
except TypeError:
    print("TypeError: нельзя вычислить длину числа.")

# ValueError
try:
    int("abc")
except ValueError:
    print("ValueError: невозможно преобразовать строку в число.")

# FileNotFoundError
try:
    open("nonexistent_file.txt")
except FileNotFoundError:
    print("FileNotFoundError: файл не найден.")

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("IndexError: индекс вне диапазона.")

# KeyError
try:
    d = {"name": "Döner"}
    print(d["age"])
except KeyError:
    print("KeyError: ключ 'age' отсутствует в словаре.")


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
else:
    print(f"Результат деления: {result}")
finally:
    print("Операция завершена.")
