import non_derivative_minimization
import descent_methods
import numpy as np
import matplotlib.pyplot as plt

def function(x: np.matrix):
    x1 = x.item(0)
    x2 = x.item(1)

    return np.matrix([[100*(x1**2 -x2)**2 + (x1-1)**2]])

def gradient(x: np.matrix):
    x1 = x.item(0)
    x2 = x.item(1)
    return np.matrix([[2*(200*x1*(x1**2-x2)+x1-1)], [-200*(x1**2-x2)]])

def hessian(x: np.matrix):
    x1 = x.item(0)
    x2 = x.item(1)

    return np.matrix([
        [1200*x1**2 - 400*x2 + 2, -400*x1],
        [-400*x1, 200*x2]
    ])

# def function(x: np.matrix):
#     return x.T*np.matrix([[4, 0], [0, 1]])*x
#
# def gradient(x: np.matrix):
#     return 2 * np.matrix([[4, 0], [0, 1]]) * x
#
# def hessian(x: np.matrix):
#     return 2 * np.matrix([[4, 0], [0, 1]])

def makeData():
    x = np.arange(-4, 4, 0.05)
    y = np.arange(-4, 4, 0.05)
    xgrid, ygrid = np.meshgrid(x, y)


    zgrid = [[function(np.matrix([[x[i]], [y[j]]])).item(0) for i in range(len(x))] for j in range(len(y))]
    return xgrid, ygrid, zgrid

# point, path = descent_methods.gradient_descent(function, gradient, point=np.matrix([[2], [2]]), step=1, epsilon=0.002, print_data=True)
# point, path = descent_methods.fastest_descent(function, gradient, point=np.matrix([[1], [2]]), epsilon=0.002, liniar_method="FIBONACCI")
# point, path = descent_methods.conjugate_gradient(function, gradient, point=np.matrix([[1], [2]]), epsilon=0.002, liniar_method="FIBONACCI")
point, path = descent_methods.newton(function, gradient, hessian, point=np.matrix([[1], [2]]), step=1, epsilon=0.002)
print(path)
print(f"Iterations: {len(path)}")

x, y, z = makeData()
cntr = plt.contour(x, y, z, 15)
plt.clabel(cntr)

plt.plot([x[0][0] for x in path], [y[1][0] for y in path], 'go-', linewidth=2)
plt.show()


# phi = (5 ** 0.5 + 1) / 2
# fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)
#
#
# a = 6
# b = 10
# eps = 1e-15
# # func = lambda x: math.log(x)*math.sin(x)*x*x if a < x <= b else 2
# func = lambda x: math.log(x**2) + 1 - math.sin(x)
# for i in range(0, 100000):
#     if fib_n(i) > (b-a)/eps:
#         iteration_limit = i+1
#         break
#
# for i in range(1, 100):
#     iter_num, value = non_derivative_minimization.golden_ratio(func, a, b, eps)
#     print(f"{iter_num}", end=" ")
#
#     iter_num, value = non_derivative_minimization.fibonacci(func, a, b, iteration_limit, eps)
#     print(f"{iter_num}", end=" ")
#
#     iter_num, value = non_derivative_minimization.combined_fibonachi(func, a, b, eps, 0.01*i)
#     print(f"{iter_num}")
#
#
#
# # iter_num, value = non_derivative_minimization.dichotomy(func, a, b, eps)
# # print(f"Dichotomy: {iter_num:5} {value:8.6f}")
# #
#
# iter_num, value = non_derivative_minimization.golden_ratio(func, a, b, eps)
# print(f"Golden Ratio: {iter_num:5} {value:8.6f}")
#
# iter_num, value = non_derivative_minimization.fibonacci(func, a, b, iteration_limit, eps)
# print(f"Fibonacci: {iter_num:5} {value:8.6f}")
#
# # iter_num, value = non_derivative_minimization.parabola_method(func, a, b, eps, True)
# # print(f"Parabola: {iter_num:5} {value:8.6f}")
# #
# # iter_num, value = non_derivative_minimization.brent_method(func, a, b, eps)
# # print(f"Brent's: {iter_num:5} {value:8.6f}")
#
# iter_num, value = non_derivative_minimization.combined_fibonachi(func, a, b, eps, 0.05)
# print(f"Fib+Gold's: {iter_num:5} {value:8.6f}")
#

