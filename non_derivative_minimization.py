import random


def dichotomy(function, a, b, epsilon, print_data=False):
    iterations = 0
    delta = epsilon / 2
    while b - a >= 2 * epsilon:
        iterations += 1
        if print_data:
            print(f"Iteration: {iterations}  Limits [{a} {b}]")
        c = (a + b) / 2
        if function(c + delta) > function(c - delta):
            b = c + delta
        else:
            a = c - delta

    return iterations, (a + b) / 2


def golden_ratio(function, a, b, epsilon, print_data=False):
    ratio = (3 - 5 ** 0.5) / 2
    iterations = 0

    x1 = a + ratio * (b - a)
    x2 = b - ratio * (b - a)

    f1 = function(x1)
    f2 = function(x2)

    while b - a >= epsilon:
        iterations += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + ratio * (b - a)
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - ratio * (b - a)
            f2 = function(x2)

        if print_data:
            print(f"Iteration: {iterations}  Limits [{a} {b}]")

    return iterations, (a + b) / 2


def fibonacci(function, a, b, iteration_limit, epsilon,  print_data=False, start_iteration = 0):
    phi = (5 ** 0.5 + 1) / 2
    fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)

    k = 1

    x1 = a + fib_n(iteration_limit-2)/fib_n(iteration_limit)*(b-a)
    x2 = a + fib_n(iteration_limit-1)/fib_n(iteration_limit)*(b-a)
    f1 = function(x1)
    f2 = function(x2)
    iteration = start_iteration
    while (b-a) >= epsilon:
        iteration += 1
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + fib_n(iteration_limit-1-iteration)/fib_n(iteration_limit-iteration)*(b-a)
            f2 = function(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + fib_n(iteration_limit-2-iteration)/fib_n(iteration_limit-iteration)*(b-a)
            f1 = function(x1)

        if print_data:
            print(f"Iteration: {iteration}  Limits [{a} {b}]")

        if iteration == iteration_limit - 2:
            x2 = x1 + epsilon/2
            if function(x1) == function(x2):
                a = x1
                b = x2
            else:
                b = x2
            break

    return iteration, (a+b)/2


def parabola_method(function, a, b, epsilon, print_data=False):
    f1 = function(a)
    f3 = function(b)

    # while True:
    #     x = a + random.random() * (b - a)
    #     f2 = function(x)
    #     if f1 > f2 and f3 > f2:
    #         break

    x = a + 0.5 * (b - a)
    f2 = function(x)

    iterations = 0
    if print_data:
        print(f"Iteration: {iterations}  Limits [{a} {b}]")

    while b - a >= epsilon:
        iterations += 1
        if (2 * ((x - a) * (f2 - f3) - (x - b) * (f2 - f1))) == 0:
            break
        u = x - ((x - a) ** 2 * (f2 - f3) - (x - b) ** 2 * (f2 - f1)) / (2 * ((x - a) * (f2 - f3) - (x - b) * (f2 - f1)))
        if u < x:
            b = x
            f3 = f2
            f2 = function(u)
            x = u
        elif u == x:
            return iterations, u
        else:
            a = x
            f1 = f2
            f2 = function(u)
            x = u
        if print_data:
            print(f"Iteration: {iterations}  Limits [{a} {x} {b}]")
            # print(f"{a} {b}")

    return iterations, (a + b) / 2


def brent_method(function, a, b, epsilon, print_data=False):
    ratio = (3 - 5 ** 0.5) / 2
    iterations = 0
    x = v = w = (a + b) / 2
    f_x = f_v = f_w = function(x)
    d = e = b - a

    while b - a >= 2 * epsilon:
        iterations += 1
        if print_data:
            print(f"Iteration: {iterations}  Limits [{a} {b}]")
        g = e
        e = d

        parabolized = False
        if x != v and x != w and v != w and f_x != f_v and f_x != f_w and f_v != f_w:
            u = x - ((x - v) ** 2 * (f_x - f_w) - (x - w) ** 2 * (f_x - f_v)) / (2 * ((x - v) * (f_x - f_w) - (x - w) * (f_x - f_v)))



            if a+epsilon <= u <= b-epsilon and abs(u-x) < g/2:
                parabolized = True
                if abs(u-x) < epsilon:
                    sign_u_without_x = abs(u-x)/(u-x) if u-x!=0 else 0
                    u = x + sign_u_without_x*epsilon
                d = abs(u-x)

        if not parabolized:
            if x < (a+b)/2:
                u = x + ratio*(b-x)
                e = b - x
                d = u - x
            else:
                u = x - ratio*(x-a)
                e = x - a
                d = x - u

        f_u = function(u)

        if f_u <= f_x:
            if u >= x:
                a = x
            else:
                b = x
            v = w
            f_v = f_w
            w = x
            f_w = f_x
            x = u
            f_x = f_u
        else:
            if u >= x:
                b = u
            else:
                a = u

            if f_u <= f_w or w == x:
                v = w
                w = u
                f_v = f_w
                f_w = f_u
            elif f_u <= f_v or v == x or v == w:
                v = u
                f_v = f_u

    return iterations, (a + b) / 2


def combined_fibonachi(function, a, b, epsilon, gold_part, print_data = False):
    ratio = (3 - 5 ** 0.5) / 2
    iterations = 0

    x1 = a + ratio * (b - a)
    x2 = b - ratio * (b - a)

    f1 = function(x1)
    f2 = function(x2)

    limit = (b - a)*gold_part

    while b - a >= limit and b-a >= epsilon:
        iterations += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + ratio * (b - a)
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - ratio * (b - a)
            f2 = function(x2)
        if print_data:
            print(f"Iteration: {iterations}  Limits [{a} {b}]")

    iteration_limit = 0
    phi = (5 ** 0.5 + 1) / 2
    fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)
    for i in range(0, 100000):
        if fib_n(i) > (b - a) / epsilon:
            iteration_limit = i + 1
            break

    return fibonacci(function, a, b, iteration_limit, epsilon, print_data, iterations)


def use_method(func, a, b, eps, method: str):
    if method == "DICHOTOMY":
        _, val = dichotomy(func, a, b, eps)
        print(f"{_=}")
        return val
    if method == "GOLDEN":
        _, val = golden_ratio(func, a, b, eps)
        print(f"{_=}")
        return val
    if method == "FIBONACCI":
        phi = (5 ** 0.5 + 1) / 2
        fib_n = lambda x: int((phi ** x - (-phi) ** (-x)) / 5 ** 0.5)
        for i in range(0, 100000):
            if fib_n(i) > (b-a)/eps:
                iteration_limit = i+1
                break

        _, val = fibonacci(func, a, b, iteration_limit, eps)
        print(f"{_=}")
        return val
    if method == "BRENT":
        _, val = brent_method(func, a, b, eps)
        print(f"{_=}")
        return val
    if method == "PARABOLA":
        print(f"{_=}")
        _, val = parabola_method(func, a, b, eps)
        return val
