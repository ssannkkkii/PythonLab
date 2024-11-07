# Ініціалізація бази даних
database = []

# Функція для виведення меню
def print_menu():
    print("\nОберіть операцію:")
    print("a. Вивести всю БД")
    print("b. Додати елемент до БД")
    print("c. Відсортувати БД за заданим атрибутом")
    print("d. Видалити елемент за індексом")
    print("e. Видалити елемент за значенням атрибуту")
    print("f. Вивести всі елементи за заданим атрибутом")
    print("q. Вийти")

# Основний цикл програми
while True:
    print_menu()
    choice = input("Введіть ваш вибір: ").strip().lower()
    
    # a. Вивести всю БД
    if choice == 'a':
        if not database:
            print("База даних порожня.")
        else:
            for i, film in enumerate(database):
                print(f"{i + 1}. {film}")

    # b. Додати елемент до БД
    elif choice == 'b':
        film = {}
        film['Назва'] = input("Введіть назву фільму: ")
        film['Режисер'] = input("Введіть ім'я режисера: ")
        film['Рік випуску'] = input("Введіть рік випуску: ")
        film['Бюджет'] = input("Введіть бюджет фільму: ")
        film['Тривалість'] = input("Введіть тривалість фільму (у хвилинах): ")
        film['Розмір файлу'] = input("Введіть розмір файлу (у МБ): ")
        database.append(film)
        print("Фільм додано до БД.")

    # c. Відсортувати БД за заданим атрибутом
    elif choice == 'c':
        if not database:
            print("База даних порожня.")
        else:
            attribute = input("Введіть атрибут для сортування (Назва, Режисер, Рік випуску, Бюджет, Тривалість, Розмір файлу): ").strip()
            try:
                database.sort(key=lambda x: x[attribute])
                print(f"БД відсортовано за атрибутом '{attribute}'.")
            except KeyError:
                print(f"Атрибут '{attribute}' не знайдено.")

    # d. Видалити елемент за індексом
    elif choice == 'd':
        index = int(input("Введіть індекс для видалення (починаючи з 1): ")) - 1
        if 0 <= index < len(database):
            deleted_film = database.pop(index)
            print("Фільм видалено:", deleted_film)
        else:
            print("Неправильний індекс.")

    # e. Видалити елемент за значенням атрибуту
    elif choice == 'e':
        attribute = input("Введіть атрибут для видалення (Назва, Режисер, Рік випуску, Бюджет, Тривалість, Розмір файлу): ").strip()
        value = input(f"Введіть значення атрибуту '{attribute}' для видалення: ").strip()
        removed = False
        for film in database:
            if film.get(attribute) == value:
                database.remove(film)
                print("Фільм видалено:", film)
                removed = True
                break
        if not removed:
            print(f"Фільм з {attribute}='{value}' не знайдено.")

    # f. Вивести всі елементи за заданим атрибутом
    elif choice == 'f':
        attribute = input("Введіть атрибут для відображення (Назва, Режисер, Рік випуску, Бюджет, Тривалість, Розмір файлу): ").strip()
        if not database:
            print("База даних порожня.")
        else:
            for film in database:
                print(film.get(attribute, "Атрибут не знайдено"))

    # q. Вийти
    elif choice == 'q':
        print("Вихід з програми.")
        break

    # Невідомий вибір
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
