# Початковий список фільмів
movies = [
    ["Inception", "Christopher Nolan", 2010, 160, 148, 2.5],
    ["The Matrix", "Lana Wachowski, Lilly Wachowski", 1999, 63, 136, 1.8],
    ["Interstellar", "Christopher Nolan", 2014, 165, 169, 3.2],
    ["The Godfather", "Francis Ford Coppola", 1972, 6, 175, 1.3],
    ["Pulp Fiction", "Quentin Tarantino", 1994, 8, 154, 1.4]
]

# Функція для виведення списку
def print_list():
    print(f"{'Назва':<20} {'Режисер':<30} {'Рік':<10} {'Бюджет, млн':<12} {'Тривалість, хв':<15} {'Розмір файлу, ГБ':<15}")
    for i, movie in enumerate(movies, start=1):
        print(f"{i:<3} {movie[0]:<20} {movie[1]:<30} {movie[2]:<10} {movie[3]:<12} {movie[4]:<15} {movie[5]:<15}")

# Функція для додавання нового фільму
def add_movie():
    name = input("Введіть назву фільму: ")
    director = input("Введіть режисера: ")
    year = int(input("Введіть рік випуску: "))
    budget = float(input("Введіть бюджет, млн: "))
    duration = int(input("Введіть тривалість, хв: "))
    file_size = float(input("Введіть розмір файлу, ГБ: "))
    movies.append([name, director, year, budget, duration, file_size])

# Функція для сортування списку за заданим атрибутом
def sort_list():
    attribute = input("Сортувати за атрибутом (назва, режисер, рік, бюджет, тривалість, розмір файлу): ").lower()
    attributes = {"назва": 0, "режисер": 1, "рік": 2, "бюджет": 3, "тривалість": 4, "розмір файлу": 5}
    if attribute in attributes:
        movies.sort(key=lambda x: x[attributes[attribute]])
        print("Список відсортовано.")
    else:
        print("Невірний атрибут.")

# Функція для видалення фільму за атрибутом
def delete_by_attribute():
    attribute = input("Видалити за атрибутом (назва, режисер, рік, бюджет, тривалість, розмір файлу): ").lower()
    value = input("Введіть значення атрибута: ")
    attributes = {"назва": 0, "режисер": 1, "рік": 2, "бюджет": 3, "тривалість": 4, "розмір файлу": 5}
    if attribute in attributes:
        movies[:] = [movie for movie in movies if str(movie[attributes[attribute]]) != value]
        print("Елементи видалено.")
    else:
        print("Невірний атрибут.")

# Функція для видалення фільму за індексом
def delete_by_index():
    index = int(input("Введіть індекс для видалення: ")) - 1
    if 0 <= index < len(movies):
        movies.pop(index)
        print("Елемент видалено.")
    else:
        print("Невірний індекс.")

# Функція для виведення фільмів за атрибутом
def display_by_attribute():
    attribute = input("Вивести за атрибутом (назва, режисер, рік, бюджет, тривалість, розмір файлу): ").lower()
    value = input("Введіть значення атрибута: ")
    attributes = {"назва": 0, "режисер": 1, "рік": 2, "бюджет": 3, "тривалість": 4, "розмір файлу": 5}
    if attribute in attributes:
        print_list_header()
        for movie in movies:
            if str(movie[attributes[attribute]]) == value:
                print_movie(movie)
    else:
        print("Невірний атрибут.")

# Головне меню
def main():
    while True:
        print("\nМеню")
        print("1 - Друк списку")
        print("2 - Додати елемент до списку")
        print("3 - Відсортувати список за заданим атрибутом")
        print("4 - Видалити елемент за заданим атрибутом")
        print("5 - Видалити елемент за заданим індексом")
        print("6 - Вивести елементи із заданим атрибутом")
        print("7 - Вихід")
        choice = input("Виберіть операцію натиснувши відповідну цифру: ")
        if choice == "1":
            print_list()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            sort_list()
        elif choice == "4":
            delete_by_attribute()
        elif choice == "5":
            delete_by_index()
        elif choice == "6":
            display_by_attribute()
        elif choice == "7":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск програми
main()
