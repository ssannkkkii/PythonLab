import math

print("Варіант - 22\nКБ-302\nЮра Чупа\n\n")

x = float(input("Ведіть X: "))
y = float(input("Ведіть Y: "))
z = float(input("Ведіть Z: "))

calculate = 13 * z * y + math.log(x/y) - math.sqrt(17 * math.sin(x**2 - y + math.sin(z)))
format = round(calculate, 4)


print(f"Результат роботи програми: " + str(format))