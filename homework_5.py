"""There is my homework #5"""
# HW 5
# 1. Заменить символ “#” на символ “/” в строке
# 'www.my_site.com#about'
site_url = 'www.my_site.com#about'
site_url_2 = site_url.replace('#', '/')
print(site_url_2)

# 2. Напишите программу, которая добавляет ‘ing’ к словам
word = input('Enter a word: ')
print(word + 'ing')

# 3. В строке “Ivanou Ivan” поменяйте местами слова
# => "Ivan Ivanou"
full_name = "Ivanou Ivan"
new_full_name = full_name.split()[::-1]
print(' '.join(new_full_name))

# 4. Напишите программу которая удаляет пробел в начале, в конце
# строки
first_string = input("Enter string: ")
second_string = first_string.strip()
print(second_string)

# 5. Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно
# соответствовало этому утверждению:
# "pARiS" >> "Paris"
name = "pARiS"
print(name.capitalize())
