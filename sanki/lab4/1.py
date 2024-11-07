# табулювання функцій
import math

a = 0.5
b = 0.8
h = 0.02


def func(x):
    if x < 0.6:
        return math.exp(x - math.sin(x))
    elif 0.6 <= x < 0.7:
        return math.tan(math.log(abs(x)))
    elif x >= 0.7:
        return math.atan(x**7)
    else:
        return None 


x = a
print(f"{'x':^15} {'y':^15}")
print("-" * 27)
while x <= b:
    y = func(x)
    if y is not None:
        print(f"{x:10.4f} {y:15.4f}")
    x += h

