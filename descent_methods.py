import non_derivative_minimization
import numpy as np

def gradient_descent(function, gradient, point, step, epsilon, print_data=False):

    points = [point.tolist()]
    f_prev = function(point)

    counter = 0

    while np.linalg.norm(gradient(point), np.inf) > epsilon:
        counter += 1
        x = point - step*gradient(point)
        f_cur = function(x)

        if f_cur < f_prev:
            point = x
            points.append(point.tolist())
            f_prev = f_cur
            if print_data:
                print(point)
        else:
            step /= 2

    return point, points


def fastest_descent(function, gradient, point, epsilon, liniar_method, print_data=False):
    points = [point.tolist()]

    while np.linalg.norm(gradient(point), np.inf) > epsilon:
        min_func = lambda a: function(point - a*gradient(point))
        step = non_derivative_minimization.use_method(min_func, 0, 1, epsilon, liniar_method)
        point = point - step*gradient(point)
        points.append(point.tolist())

    return point, points

def conjugate_gradient(function, gradient, point, epsilon, liniar_method):
    points = [point.tolist()]
    p = -gradient(point)
    prev_point = point

    while np.linalg.norm(gradient(point), np.inf) > epsilon:
        min_func = lambda a: function(point + a * p)
        a_step = non_derivative_minimization.use_method(min_func, 0, 1, epsilon, liniar_method)
        point = point + a_step * p
        points.append(point.tolist())

        b = -(np.linalg.norm(gradient(point), np.inf)/np.linalg.norm(gradient(prev_point), np.inf))**2
        p = -gradient(point) + b * p
        prev_point = point

    return point, points


def newton(function, gradient, hessian, point, step, epsilon):
    points = [point.tolist()]
    f_prev = function(point)
    counter = 0

    while np.linalg.norm(gradient(point), np.inf) > epsilon:
        counter += 1
        x = point - step * hessian(point).I * gradient(point)
        f_cur = function(x)

        if f_cur < f_prev:
            point = x
            points.append(point.tolist())
            f_prev = f_cur
        else:
            step /= 2

    return point, points