import non_derivative_minimization
import math

# phi = (5 ** 0.5 + 1) / 2
# fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)

func = lambda x: -math.sin(x)
a = -1
b = 4
eps = 0.0001
iteration_limit = 25

iter_num, value = non_derivative_minimization.dichotomy(func, a, b, eps)
print(f"Dichotomy: {iter_num:5} {value:8.4f}")

iter_num, value = non_derivative_minimization.golden_ratio(func, a, b, eps)
print(f"Golden Ratio: {iter_num:5} {value:8.4f}")

iter_num, value = non_derivative_minimization.fibonacci(func, a, b, iteration_limit)
print(f"Fibonacci: {iter_num:5} {value:8.4f}")

iter_num, value = non_derivative_minimization.parabola_method(func, a, b, eps)
print(f"Parabola: {iter_num:5} {value:8.4f}")

iter_num, value = non_derivative_minimization.brent_method(func, a, b, eps) #, True)
print(f"Brent's: {iter_num:5} {value:8.4f}")