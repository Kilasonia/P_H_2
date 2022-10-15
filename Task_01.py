# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. (умножаем на -3)
# Пример:
# Для N = 5 : 1, -3,9,-27,81

# n = int(input('Введите число N : '))
# for i in range(n):
#     result = (-3)**i
#     print(result, end=" ")


# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.

# str_1 = str(input(" Enter the string str_1 : "))
# str_2 = str(input(" Enter the string str_2 : "))


# def str_count(str, substr):
#     return 0 if len(str) < len(substr) else str.startswith(substr) + str_count(str[1:], substr)


# print(str_count(str_1, str_2))


# Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

# n = int(input("Введите число N : "))
# d = {i: 3*i + 1 for i in range(1, n+1)}
# print(f"Итоговая последовательность : {d}")
