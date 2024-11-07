import math

a = -1
b = 1
h = 0.5
d = 0.001

def series_sum(x, d):
    sum_val = 1.0  
    k = 1
    term = 1.0
    while abs(term) > d:
        term = ((-1) ** k) * x / (k * (k + 1)) * math.sin(2 + k + 1)
        sum_val += term
        k += 1 
    return sum_val

x = a
print(f"{'x':>10} {'y(x)':>10} {'Похибка':>10}")
while x <= b:
    y = series_sum(x, d)
    print(f"{x:10.5f} {y:10.5f} {d:10.5f}")
    x += h
