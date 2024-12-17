def is_in_line_1(x, y, a, b):
    if(y == a*x + b):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")

def is_in_line_2(x, y, xa, ya, xb, yb):
    if((y-ya)*(xb-xa)-(x-xa)*(yb-ya) == 0):
        return("Punkt należy do prostej")
    else:
        return("Punkt nie należy do prostej")


if __name__ == '__main__':
    print("Podaj współrzędne x i y punktu")
    x = int(input("x: "))
    y = int(input("y: "))

    print("Podaj współczynniki a i b równania prostej w postaci kierunkowej")
    a = int(input("a: "))
    b = int(input("b: "))

    print("Podaj współrzędne x i y punktów A i B należących do prostej")
    xA = int(input("xA: "))
    yA = int(input("yA: "))
    xB = int(input("xB: "))
    yB = int(input("yB: "))

    print(is_in_line_1(x, y, a, b))
    print(is_in_line_2(x, y, xA, yA, xB, yB))