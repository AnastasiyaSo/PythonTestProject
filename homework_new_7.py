"""My Homework 7"""
# Task #1
import random

rules = """Привет!\nПеред Вами игра \"Быки и коровы\".
Правила игры:
1. Компьютер загадывает 4-значное число с неповторяющимися цифрами.
2. Ваша задача - попытаться отгадать число.
3. Попытка — это ввод 4-значного числа с неповторяющимися цифрами.
4. Компьютер сообщает в ответ:
- кол-во быков - сколько цифр угадано вплоть до позиции
- кол-во коров - сколько цифр угадано без совпадения с их позициями в числе
5. Компьютер предлагает снова попытаться угадать число.
6. Количество попыток не ограниченно.
"""
print(rules)

while True:
    start_of_game = input("Вы готовы начать игру? "
                          "Введите \"Y\", если готовы начать или \"N\" "
                          "для выхода из игры: ").upper()

    if start_of_game == 'Y':
        random_number = list(random.sample(range(0, 10), 4))

        user_number = [int(i)
                       for i in list(
                input("Введите 4-значное число "
                      "с неповторяющимися цифрами: "))]
        while user_number != random_number:
            count_of_cows = 0
            count_of_bulls = 0
            index_of_random_number = 0
            for i in user_number:
                if i == random_number[index_of_random_number]:
                    count_of_bulls += 1
                    index_of_random_number += 1
                    if i in random_number:
                        count_of_cows += 1

                print(f"Количество быков: {count_of_bulls}, "
                      f"количество коров: {count_of_cows}")

                user_number = [int(i)
                               for i in list(
                        input("Введите 4-значное число "
                              "с неповторяющимися цифрами: "))]

            print("Вы выиграли!")
            break
    elif start_of_game == 'N':
        print("До новых встреч!")
        break
    else:
        print("Ошибка ввода!")
        continue

# Task #2

n = 10
spaces = n - 1
asterisks = 1

while n != 0:
    print(" " * spaces, "*" * asterisks)
    n -= 1
    spaces -= 1
    asterisks += 2

# Task #3

first_list = [6, 2, 3, 8]
first_list.sort()
min_value = first_list[0]
max_value = max(first_list)
second_list = list(range(min_value, max_value + 1))
missing_list = list(set(second_list) - set(first_list))
print(f"Количество отсутствующих статуй: {len(missing_list)}, "
      f"у Вас отсутствуют статуи: {missing_list}")
