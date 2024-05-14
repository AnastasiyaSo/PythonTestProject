"""There is my homework # 6"""
# HW 6
# 1. Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
string_1 = "Robin Singh"
list_1 = string_1.split()
print(type(list_1), ":", list_1)
# 2. Перевести строку в список
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
string_2 = "I love arrays they are my favorite"
list_2 = string_2.split()
print(type(list_2), ":", list_2)
# 3. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
list_3 = ["Ivan", "Ivanou"]
string_3 = "Minks"
string_4 = "Belarus"
string_5 = " ".join(list_3)
print(f"Привет, {string_5}! Добро пожаловать в {string_3} {string_4}")
# 4. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
list_4 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string_6 = " ".join(list_4)
print(type(string_6), ":", string_6)
# 5. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
list_5 = [1, 2 ,3, "word", 5, "next", 6, "@", "$", 9, 10]
list_5.insert(3, "new value")
list_5.pop(6)
print(list_5)
