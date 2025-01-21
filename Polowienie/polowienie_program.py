# liczenie wartości funkcji schematem Hornera
def f(x):
    result = COEFFICIENTS[0]
    for i in range(1, DEGREE + 1):
        result = result * x + COEFFICIENTS[i]

    return result

# pobieranie wzoru funkcji
def get_function_data():
    coefficients = []
    degree = int(input("Enter degree of polynomial: "))
    for i in range(degree, -1, -1):
        coefficients.append(float(input(f"Enter the coefficient of power {i}: ")))

    return coefficients, degree

# algorytm polowienie (bisekcji)
def bisection(a, b, EPSX, EPS0):
    fa = f(a)
    fb = f(b)
    if fa == 0: return a
    if fb == 0: return b
        
    if fa * fb >= 0:
        print("Function doesn't meet requirements.")
        return

    mid = a
    # sprawdzanie czy znaleziony pierwiastek jest wyznaczony dostatecznie dokladnie
    while abs(b-a) > EPSX:
        mid = (a + b) / 2

        # sprawdzanie czy f(mid) jest wystarczajaco bliska 0
        if abs(f(mid)) < EPS0:
            return mid

        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid

    return (a+b)/2


COEFFICIENTS = []
DEGREE = 0

if __name__ == '__main__':
    data = get_function_data()
    COEFFICIENTS = data[0]
    DEGREE = data[1]

    print("Range, in which the function will be analysed: ")
    a = float(input("Minimum :"))
    b = float(input("Maximum :"))

    decimal_places = int(input("Precision (number of decimal places):"))
    precision = pow(10, -1 * decimal_places)


    print(f"Zero of the function = {round(bisection(a, b, precision, precision), decimal_places)}")

