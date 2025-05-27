
def dywan_sierpinskiego(z, stopien, dl_bok):

    def kwadrat(bok, kolor):
        z.color(kolor)
        z.begin_fill()
        for i in range(4):
            z.forward(bok)
            z.right(90)
        z.end_fill()

    if stopien == 0:
        kwadrat(dl_bok, 'black')
        return None
    else:
        kwadrat(dl_bok, 'white')
        for i in range(4):
            for j in range(2):
                dywan_sierpinskiego(z, stopien-1, dl_bok/3)
                z.forward(dl_bok/3)
            z.forward(dl_bok/3)
            z.right(90)
