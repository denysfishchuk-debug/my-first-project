# Lists Списки Listen
list_empty = []
list_values = [1, 2, 3]
list_from_tuple = list((4, 5, 6))
print("Lists:", list_empty, list_values, list_from_tuple)

# Tuples Кортежи Tupeln
tuple_empty = ()
tuple_values = (10, 20, 30)
tuple_from_list = tuple([40, 50, 60])
print("Tuples:", tuple_empty, tuple_values, tuple_from_list)

# Dictionaries Словари 
dict_empty = {}
dict_values = {'a': 1, 'b': 2}
dict_from_list = dict([('x', 100), ('y', 200)])
print("Dictionaries:", dict_empty, dict_values, dict_from_list)

# Sets Множества Mengen
set_empty = set()
set_values = {1, 2, 3}
set_from_tuple = set((2, 3, 4, 4))
print("Sets:", set_empty, set_values, set_from_tuple)

print("\n--- Element Access and Manipulation: The Power of Operations ---")

# List Списки Listen
my_list = [10, 20, 30, 40, 50]
print(my_list[0], my_list[-1])        # Index access
print(my_list[1:4])                   # Slicing

my_list.append(60)                    # Add at end добавление в конец
my_list.insert(0, 5)                  # Add at beginning добавление в начало
my_list.insert(3, 25)                 # Add at position добавление в конкретную позицию
my_list.remove(30)                    # Remove by value удаление по значению
del my_list[2]                        # Remove by index удаление по индексу
my_list[1] = 15                       # Modify element изменение значения элемента
print("Modified List:", my_list)

# Tuple Кортежи Tupeln
my_tuple = (1, 2, 3)
print(my_tuple[0], my_tuple[-1]) # доступ по индексу
print(my_tuple[0:2]) # срез кортежа


# Кортежи неизменяемы нельзя напрямую изменить, добавить или удалить элементы
# Чтобы "изменить" кортеж, преобразуем его в список и обратно

temp = list(my_tuple)
temp.append(4)
my_tuple = tuple(temp)
print("Modified Tuple:", my_tuple)


# Dictionaries Словари 
my_dict = {'name': 'Alice', 'age': 30, 'city': 'Berlin'}
print(my_dict['name'])  # доступ к значению по ключу

my_dict['country'] = 'Germany'  # добавление новой пары
my_dict['age'] = 31  # изменение значения по ключу
del my_dict['city']  # удаление пары по ключу
print("Изменённый словарь:", my_dict)


# Sets Множества Mengen
my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # добавление одного элемента
my_set.update([7, 8])  # добавление нескольких элементов
my_set.remove(2)  # удаление элемента
my_set.add(3)  # попытка добавить дубликат (не изменит множество)
print("Изменённое множество:", my_set)



print("\n--- 3 Iteration über Datenstrukturen ---")

# Итерация по структурам данных
numbers = [1, 2, 3, 4]
words = ("hello", "world", "python")
people = {'Alice': 30, 'Bob': 25, 'Charlie': 35}
letters = {'a', 'b', 'c'}

for num in numbers:
    print("Элемент списка:", num)

for word in words:
    print("Элемент кортежа:", word)

for key in people:
    print("Ключ словаря:", key)

for value in people.values():
    print("Значение словаря:", value)

for key, value in people.items():
    print(f"{key} — возраст {value}")

for letter in letters:
    print("Элемент множества:", letter)


sentence = "This is a test sentence this is good"
words = sentence.lower().split()  
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1  

print("results:", word_count)
