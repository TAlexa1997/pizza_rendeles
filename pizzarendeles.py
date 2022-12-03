def pizza():
    print(f"Jó napot kívánok! Vanda vagyok a megrendelést segítő robot!")
    tipus = []
    meret = []
    feltet = []
    ar = []
    i = 0
    kilep = False
    while not kilep:
        print(f"Milyen pizzát szeretne rendelni? Van gombás,sajtos illetve sonkás pizzánk!")
        print(f"Ha már nem szeretnél rendelni kérlek írj egy '@' jelet!")
        akt_ar = 0
        fajta = input()
        if fajta == "sajtos":
            akt_ar = 1000
        elif fajta == "gombás":
            akt_ar = 1100
        elif fajta == "sonkás":
            akt_ar = 1200
        elif fajta == "@":
            kilep = True
            continue
        else:
            print(f"Sajnos ilyen választási lehetőség nincs!")
            continue
        print(f"Mekkora méretben szeretne rendelni pizzát?Kicsi,normál vagy nagy?")
        nagysag = input()
        if nagysag == "kicsi":
            akt_ar *= 0.9
        elif nagysag == "normál":
            pass
        elif nagysag == "nagy":
            akt_ar *= 1.1
        else:
            print(f"Sajnos ilyen választási lehetőség nincs!")
            continue
        print(f"Kérsz rá plusz feltétet?i/n")
        plusz = input()
        # feltet.append(plusz == 'i')
        if plusz == "i":
            akt_ar += 50
        elif plusz == "n":
            pass
        else:
            print(f"Sajnos ilyen választási lehetőség nincs")
            continue
        tipus.append(fajta)
        ar.append(akt_ar)
        meret.append(nagysag)
        feltet.append(plusz == 'i')
    j = 0
    while j < len(tipus):
        if feltet[j]:
            ker = "kértél"
        else:
            ker = "nem kértél"
        print(f"Rendeltél egy {tipus[j]} pizzát {meret[j]} méretben amire {ker} plusz feltétet.Az ára összesen: {ar[j]:.0f}")
        j += 1
    print(f"Tehát összesen a rendelésed értéke: {sum(ar):.0f}")


