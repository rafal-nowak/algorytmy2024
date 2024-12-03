def f(x):
    y = x ** 3 - 2 * x ** 2 + 2 * x - 4
    return y


if __name__ == '__main__':
    a = -4
    b = 4
    c = 0
    tolerance = 0.001

    if f(a) * f(b) > 0:
        print("Incorrect function.")
    else:
        while abs(a - b) > tolerance:
            c = (a + b) / 2
            if f(c) == 0:
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c

        print((a + b) / 2)
        
