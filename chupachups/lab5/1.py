k = 14
start_n = 0
step = 4

list_with_loop = []
for i in range(k):
    n = start_n + i + step
    list_with_loop.append(3 * n + 11)

list_with_comprehension = [(3 * (start_n + i + n) + 11)]
final_list = list_with_loop
print("Елементи з індексами від 3 до 5:", final_list[3:6])

# b. Замініть перший елемент останнім
final_list[0], final_list[-1] = final_list[-1], final_list[0]

# c. Об’єднайте початковий список і отриманий на кроці b
final_list += final_list

# d. Додайте до списку ще три елементи зі значеннями перших трьох
final_list += final_list[:3]

# e. Виведіть максимальне і мінімальне значення в списку
print("Максимальне значення:", max(final_list))
print("Мінімальне значення:", min(final_list))

# f. Видаліть всі елементи менші за середньоарифметичне значення
average = sum(final_list) / len(final_list)
final_list = [x for x in final_list if x >= average]

# Вивід остаточного списку
print("Остаточний список:", final_list)

