import math

print("Варіант - 6\nКБ-302\nГреділь Олександр\n\n")

x = float(input("Ведіть X: "))
y = float(input("Ведіть Y: "))

calculate = 2 * math.cos(y) + math.sqrt(math.sin(x)**4) + math.log(4, 1 + abs(math.sin(y) / (x**4 - y**4)))
result = math.ceil(calculate)

print(f"Результат роботи програми: " + str(result))