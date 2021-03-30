import non_derivative_minimization
import math

phi = (5 ** 0.5 + 1) / 2
fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)

func = lambda x: math.sin(x)*x
a = -5
b = -2
eps = 1e-5
for i in range(0, 100000):
    if fib_n(i) > (b-a)/eps:
        iteration_limit = i+1
        break

for i in range(15):
    eps = 1/10**i

    for i in range(0, 100000):
        if fib_n(i) > (b - a) / eps:
            iteration_limit = i + 1
            break

    iter_num, value = non_derivative_minimization.brent_method(func, a, b, eps)
    print(f"{iter_num:4}")



# iter_num, value = non_derivative_minimization.dichotomy(func, a, b, eps, True)
# print(f"Dichotomy: {iter_num:5} {value:8.6f}")

#
# iter_num, value = non_derivative_minimization.golden_ratio(func, a, b, eps, True)
# print(f"Golden Ratio: {iter_num:5} {value:8.6f}")
#
# iter_num, value = non_derivative_minimization.fibonacci(func, a, b, iteration_limit, eps, True)
# print(f"Fibonacci: {iter_num:5} {value:8.6f}")
#
# iter_num, value = non_derivative_minimization.parabola_method(func, a, b, eps, True)
# print(f"Parabola: {iter_num:5} {value:8.6f}")
#
# iter_num, value = non_derivative_minimization.brent_method(func, a, b, eps, True)
# print(f"Brent's: {iter_num:5} {value:8.6f}")