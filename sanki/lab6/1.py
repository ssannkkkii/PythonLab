# Формула: n^2 + 3n + 5
def formula(n):
    return n**2 + 3 * n + 5

# Параметри
n = 1
step = 4
num_elements = 17

# Створення кортежу з 17 елементів за формулою
initial_tuple = tuple(formula(n + step * i) for i in range(num_elements))
print("Початковий кортеж:", initial_tuple)

# a. Виведіть елементи з індексами від 3 до 5
print("Елементи з індексами від 3 до 5:", initial_tuple[3:6])

# b. Замініть перший елемент останнім
modified_tuple = (initial_tuple[-1],) + initial_tuple[1:]
print("Кортеж після заміни першого елемента останнім:", modified_tuple)

# c. Об’єднайте початковий кортеж і отриманий на кроці b
combined_tuple = initial_tuple + modified_tuple
print("Об'єднаний кортеж:", combined_tuple)

# d. Додайте до кортежу ще три елементи зі значеннями перших трьох
extended_tuple = combined_tuple + combined_tuple[:3]
print("Кортеж після додавання перших трьох елементів ще раз:", extended_tuple)

# e. Виведіть максимальне і мінімальне значення в кортежі
print("Максимальне значення в кортежі:", max(extended_tuple))
print("Мінімальне значення в кортежі:", min(extended_tuple))
# f. Видаліть всі елементи менші за середньоарифметичне значення
average_value = sum(extended_tuple) / len(extended_tuple)
filtered_tuple = tuple(x for x in extended_tuple if x >= average_value)
print("Кортеж після видалення елементів менших за середнє арифметичне:", filtered_tuple)
