import random
import string

password_length = 7

#low_char(2) + num_char(3) + spc_char(2)

num_lowercase = 2
num_digits = 3
num_special_chars = 2

digits = ''.join(random.sample(string.digits, num_digits))
lowercase = ''.join(random.sample(string.ascii_lowercase, num_lowercase))
special_chars = ''.join(random.sample("!@#$%^&*_-)(", num_special_chars))


password = digits + lowercase + special_chars

password = ''.join(random.sample(password, len(password)))

print("Згенерований пароль:", password)

