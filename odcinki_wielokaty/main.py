from __future__ import annotations

Punkt = tuple[float, float]


class Prosta:
    def __init__(self, a: float, b: float, c: float):
        if (a, b) == (0, 0):
            raise ValueError("a i b nie mogą jednocześnie wynosić 0")
        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, prosta2):
        if isinstance(prosta2, Prosta):
            W = (self.a*prosta2.b)-(prosta2.a*self.b)
            Wx = -(self.c*prosta2.b)+(prosta2.c*self.b)
            Wy = -(self.a*prosta2.c)+(prosta2.a*self.c)
            return W == 0 and Wx == 0 and Wy == 0
        return False

    def czy_równoległa(self, prosta2: Prosta):
        W = (self.a*prosta2.b)-(prosta2.a*self.b)
        return W == 0

    def punk_przecięcia(self, prosta2: Prosta) -> Punkt:
        if self.czy_równoległa(prosta2):
            return None
        W = (self.a*prosta2.b)-(prosta2.a*self.b)
        Wx = -(self.c*prosta2.b)+(prosta2.c*self.b)
        Wy = -(self.a*prosta2.c)+(prosta2.a*self.c)

        return (Wx/W, Wy/W)


class Odcinek:
    def __init__(self, początek: Punkt, koniec: Punkt):
        if początek == koniec:
            raise ValueError("punkty muszą się od siebie różnić")

        self.początek = początek
        self.koniec = koniec

    def prosta(self):
        a = self.początek[1] - self.koniec[1]
        b = self.koniec[0] - self.początek[0]
        c = -(a*self.początek[0] + b*self.początek[1])
        return Prosta(a, b, c)

    def czy_zawiera_punkt(self, punkt: Punkt):
        x_min = min(self.początek[0], self.koniec[0])
        x_max = max(self.początek[0], self.koniec[0])
        return x_min <= punkt[0] <= x_max

    def przecina(self, odcinek2: Odcinek) -> bool:
        if not self.prosta().czy_równoległa(odcinek2.prosta()):
            punkt_przecięcia = self.prosta().punk_przecięcia(odcinek2.prosta())
            return self.czy_zawiera_punkt(punkt_przecięcia) and odcinek2.czy_zawiera_punkt(punkt_przecięcia)
        if self.prosta() == odcinek2.prosta():
            return self.czy_zawiera_punkt(odcinek2.początek) or self.czy_zawiera_punkt(odcinek2.koniec)
        else:
            return False


class Wielokąt:
    def __init__(self, *wierzchołki: Punkt):
        if len(wierzchołki) < 3:
            raise ValueError("Wielokąt musi mieć conajmniej 3 wierzchołki")
        self.wierzchołki = list(wierzchołki)

    def czy_zawiera_punkt(self, punkt: Punkt) -> bool:
        for indeks in range(len(self.wierzchołki)):
            wierzchołek1 = self.wierzchołki[indeks]
            wierzchołek2 = self.wierzchołki[(indeks+1)%len(self.wierzchołki)]
            prosta = Odcinek(wierzchołek1, wierzchołek2).prosta()

            wierzchołek3 = self.wierzchołki[(indeks+2)%len(self.wierzchołki)]

            a, b, c = prosta.a, prosta.b, prosta.c
            if (a*wierzchołek3[0] + b*wierzchołek3[1] + c) * (a*punkt[0] + b*punkt[1] + c) < 0:
                return False
        return True