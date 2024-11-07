from colorama import Fore, Style
import re

def validate_password(password):
    length = len(password)

    if length != 10:
        print(Fore.RED + "Невірна довжина паролю. Пароль повинен мати 10 символів." + Style.RESET_ALL)
        return False

    # Перевірка кількості малих латинських літер
    low_char_count = sum(1 for char in password if char.islower())
    if low_char_count < 2 or low_char_count > 4:
        print(Fore.RED + "Пароль має містити від 2 до 4 маленьких латинських літер." + Style.RESET_ALL)
        return False

    # Перевірка кількості цифр
    num_char_count = sum(1 for char in password if char.isdigit())
    if num_char_count < 3 or num_char_count > 4:
        print(Fore.RED + "Пароль має містити від 3 до 4 цифр." + Style.RESET_ALL)
        return False

    # Перевірка кількості спеціальних символів
    spc_char_count = sum(1 for char in password if not char.isalnum())
    if spc_char_count != 3:
        print(Fore.RED + "Пароль має містити точно 3 спеціальних символи." + Style.RESET_ALL)
        return False

    # Перевірка на повторення однакових спеціальних символів
    seen_special_chars = set()
    for char in password:
        if not char.isalnum():  # Якщо це спеціальний символ
            if char in seen_special_chars:
                print(Fore.RED + "Пароль не повинен містити однакових спеціальних символів." + Style.RESET_ALL)
                return False
            seen_special_chars.add(char)

    # Перевірка на повторення цифр підряд
    if len(re.findall(r'(\d)\1{2,}', password)) > 0:
        print(Fore.RED + "Пароль не повинен містити більше 3 однакових цифр підряд." + Style.RESET_ALL)
        return False

    print(Fore.GREEN + "Пароль успішно підтверджено!" + Style.RESET_ALL)
    return True

def main():
    requirements = """
    Вимоги до паролю:
        - Довжина: 10 символів
        - Не менше 2 маленьких латинських літер
        - Не більше 4 маленьких латинських літер
        - Не менше 3 цифр
        - Не більше 4 цифр
        - Точно 3 спеціальних символів
        - Не повинно бути однакових спеціальних символів 
        - Не більше 3 однакових цифр підряд
    """
    print(requirements)
    
    password = input("Будь ласка, введіть пароль: ")
    validate_password(password)

if __name__ == "__main__":
    main()
