import random
import string

password_length = 7

#low_char(6) + num_char(1) + spc_char(2) + upp_char(3)

num_lowercase = 6
num_digits = 1
num_special_chars = 2
num_upercase = 3

digits = ''.join(random.sample(string.digits, num_digits))
lowercase = ''.join(random.sample(string.ascii_lowercase, num_lowercase))
special_chars = ''.join(random.sample("!@#$%^&*_-)(", num_special_chars))
upercase = ''.join(random.sample(string.ascii_uppercase, num_upercase))


password = digits + lowercase + special_chars + upercase

password = ''.join(random.sample(password, len(password)))

print("Згенерований пароль:", password)
