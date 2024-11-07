import math

a = 0.5
b = 0.9
h = 0.5
d = 0.0001

def series_sum(x, d):
    sum_val = math.pi / 2 - x  
    n = 1
    term = 1.0
    while abs(term) > d:
        term = (2 * n - 1) / ((2 * n) * (2 * n + 1)) * (x ** (2 * n + 1))
        sum_val -= term
        n += 1
    return sum_val

x = a
print(f"{'x':>10} {'y(x)':>10} {'Похибка':>10}")
while x <= b:
    y = series_sum(x, d)
    print(f"{x:10.5f} {y:10.5f} {d:10.5f}")
    x += h
