from importlib.metadata import requires

from colorama import Fore

print("Вимоги до паролю:\n1. Не менше 10 символів. \n2. Малі цифри \n3. Має мати цифри\n4. Має мати спец. символи\n5.Має бути один символ з великою літери")
password = input("Введіть пароль: ")

required_length = 14
password_length = len(password)

is_too_short = (password_length < required_length) * (required_length - password_length)
contains_digit = any(char.isdigit() for char in password)
contains_special = any(char in "!@#$%^&*_-)(" for char in password)
contains_lower = any(char.islower() for char in password)
contains_upper = any(char.isupper() for char in password)


print(Fore.RED * (password_length < required_length) +
      Fore.GREEN * (password_length >= required_length) +
      ("Пароль короткий на " + str(is_too_short) + " символів" * (password_length < required_length) + "Довжина: ок" * (password_length >= required_length)))

print(Fore.RED * (not contains_lower) +
      Fore.GREEN * contains_lower +
      ("Пароль має містити принаймні одну малу літеру" * (not contains_lower) + "Мала літера: ок" * contains_lower))

print(Fore.RED * (not contains_digit) +
      Fore.GREEN * contains_digit +
      ("Пароль має містити принаймні одну цифру" * (not contains_digit) + "Цифра: ок" * contains_digit))

print(Fore.RED * (not contains_special) +
      Fore.GREEN * contains_special +
      ("Пароль має містити принаймні один спец. символ" * (not contains_special) + "Спец. символ: ок" * contains_special))


print(Fore.RED * (not contains_upper) +
      Fore.GREEN * contains_upper +
      ("Пароль має містити прийнамі один символ з великої літери" * (not contains_upper) + "Спец. символ: ок" * contains_upper))

print(Fore.GREEN * (password_length >= required_length and contains_digit and contains_special) +
      "\nПароль підходить" * (password_length >= required_length and contains_digit and contains_special))



