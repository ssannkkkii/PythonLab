import math

a = 2
b = 5
h = 0.2

def cot(x):
    return 1 / math.tan(x)

def cosec(x):
    return 1 / math.sin(x)

def func(x):
    if x < 3:
        return cot(x + cosec(x ** -2))
    elif 3 <= x < 4:
        return math.log10(math.log(x) + math.log(3 / x))
    elif x >= 4:
        return math.cos(5 * x**2)


x = a
print(f"{'x':^15} {'y':^15}")
print("-" * 27)
while x <= b:
    y = func(x)
    if y is not None:
        print(f"{x:10.4f} {y:15.4f}")
    x += h