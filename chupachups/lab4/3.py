from colorama import Fore, Style
import re

def validate_password(password):
    length = len(password)

    if length != 14:
        print(Fore.RED + "Невірна довжина паролю. Пароль повинен мати 14 символів." + Style.RESET_ALL)
        return False

    # Перевірка кількості малих латинських літер
    low_char_count = sum(1 for char in password if char.islower())
    if low_char_count < 5 or low_char_count > 6:
        print(Fore.RED + "Пароль має містити від 5 до 6 маленьких латинських літер." + Style.RESET_ALL)
        return False        

    # Перевірка кількості цифр
    num_char_count = sum(1 for char in password if char.isdigit())
    if num_char_count < 3 or num_char_count > 5:
        print(Fore.RED + "Пароль має містити від 3 до 5 цифр." + Style.RESET_ALL)
        return False

    # Перевірка кількості спеціальних символів
    spec_char_count = sum(1 for char in password if not char.isalnum())
    if spec_char_count < 3 or spec_char_count > 4:
        print(Fore.RED + "Пароль має містити від 3 до 4 спеціальних символів." + Style.RESET_ALL)
        return False

    # Перевірка кількості великих латинських літер
    upp_char_count = sum(1 for char in password if char.isupper())
    if upp_char_count < 3 or upp_char_count > 5:
        print(Fore.RED + "Пароль має містити від 3 до 5 великих латинських літер." + Style.RESET_ALL)
        return False

    # Перевірка на повторення однакових малих латинських літер
    if len(re.findall(r'([a-z])\1{2,}', password)) > 0:
        print(Fore.RED + "Пароль не повинен містити більше 2 однакових маленьких латинських літер підряд." + Style.RESET_ALL)
        return False

    # Перевірка на повторення однакових символів підряд
    if len(re.findall(r'(\W)\1{2,}', password)) > 0:
        print(Fore.RED + "Пароль не повинен містити більше 2 однакових спеціальних символів підряд." + Style.RESET_ALL)
        return False

    # Перевірка на повторення однакових цифр підряд
    if len(re.findall(r'(\d)\1{2,}', password)) > 0:
        print(Fore.RED + "Пароль не повинен містити більше 3 однакових цифр підряд." + Style.RESET_ALL)
        return False

    print(Fore.GREEN + "Пароль успішно підтверджено!" + Style.RESET_ALL)
    return True

def main():
    requirements = """
    Вимоги до паролю:
        - Довжина: 14 символів
        - Не менше 5 маленьких латинських літер
        - Не більше 6 маленьких латинських літер
        - Не менше 3 цифр
        - Не більше 5 цифр
        - Не менше 3 спеціальних символів
        - Не більше 4 спеціальних символів
        - Не менше 3 великих латинських літер
        - Не більше 5 великих латинських літер
        - Не більше 2 однакових маленьких латинських літер
        - Не більше 3 однакових літер підряд
    """
    print(requirements)
    
    password = input("Будь ласка, введіть пароль: ")
    validate_password(password)

if __name__ == "__main__":
    main()
