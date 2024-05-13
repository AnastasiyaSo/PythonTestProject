# HW 5
# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
siteURL = 'www.my_site.com#about'
siteURL = list(siteURL)
siteURL[15] = '/'
print(''.join(siteURL))

# 2. Напишите программу, которая добавляет ‘ing’ к словам
word = input('Enter a word: ')
print(word + 'ing')

# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
fullName = "Ivanou Ivan"
newFullName = fullName.split()[::-1]
print(' '.join(newFullName))

# 4. Напишите программу которая удаляет пробел в начале, в конце строки
firstString = input("Enter string: ")
secondString = firstString.strip()
print(secondString)

# 5. Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению:
# "pARiS" >> "Paris"
name = "pARiS"
print(name.capitalize())