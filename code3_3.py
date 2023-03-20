import getpass
import random
import sys

iloscRund = int(input("Podaj ilosc rund: "))
tryb = input("Podaj tryb:\n"
             "K - Komputer\n"
             "H - hot seat z innym graczem\n")

if (tryb != "H") & (tryb != "K"):
    print("Niepoprawna odpowiedz!")
    sys.exit(1)


nazwa1 = input("Nazwij gracza 1: ")
nazwa2 = ""
if tryb == "K" :
    nazwa2 = input("Nazwij gracza 2(komputer): ")
else:
    nazwa2 = input("Nazwij gracza 2: ")

zwyciestwa = []     #P - wygral pierwsszy, D - wygral drugi, R - remis
rundy = 0

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while rundy < iloscRund:
    rundy += 1
    print("Runda " + str(rundy))
    if tryb == "K":
        print("Wybierz swoja opcje:\n"
              "P - papier\n"
              "K - kamien\n"
              "N - nozyce\n")
        gracz1 = input(nazwa1 + ": ")
        if (gracz1 != "P") & (gracz1 != "K") & (gracz1 != "N"):
            print("Niepoprawna odpowiedz!")
            sys.exit(1)

        gracz2 = ""
        rand = random.randint(1, 3)
        if rand == 1 : gracz2 = "P"
        if rand == 2 : gracz2 = "K"
        if rand == 3 : gracz2 = "N"
        print(nazwa2 + ": " + gracz2)

        if(gracz1 == gracz2):
            zwyciestwa.append("R")
        elif gracz1 == "P":
            if gracz2 == "K":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")
        elif gracz1 == "K":
            if gracz2 == "N":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")
        elif gracz1 == "N":
            if gracz2 == "P":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")

        input("Kliknij enter dla nastepnej rundy")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print("Wybierz swoja opcje:\n"
              "P - papier\n"
              "K - kamien\n"
              "N - nozyce\n")
        gracz1 = getpass.getpass(nazwa1 + ": ")
        if (gracz1 != "P") & (gracz1 != "K") & (gracz1 != "N"):
            print("Niepoprawna odpowiedz!")
            sys.exit(1)

        gracz2 = getpass.getpass(nazwa2 + ": ")
        if (gracz2 != "P") & (gracz2 != "K") & (gracz2 != "N"):
            print("Niepoprawna odpowiedz!")
            sys.exit(1)

        print(nazwa1 + ": " + gracz1)
        print(nazwa2 + ": " + gracz2)


        if (gracz1 == gracz2):
            zwyciestwa.append("R")
        elif gracz1 == "P":
            if gracz2 == "K":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")
        elif gracz1 == "K":
            if gracz2 == "N":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")
        elif gracz1 == "N":
            if gracz2 == "P":
                zwyciestwa.append("P")
            else:
                zwyciestwa.append("D")

        input("Kliknij enter aby kontynuowac")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

zwyciestwa1 = 0
zwyciestwa2 = 0

print("\t\t\t" + nazwa1 + "\t\t\t" + nazwa2)
for index in range(0, len(zwyciestwa)):
    wynik = zwyciestwa[index]
    if wynik == "P":
        print("runda " + str(index + 1) + "\t\t\t1\t\t\t0")
        zwyciestwa1 += 1
    elif wynik == "D":
        print("runda " + str(index + 1) + "\t\t\t0\t\t\t1")
        zwyciestwa2 += 1
    else:
        print("runda " + str(index + 1) + "\t\t\t0\t\t\t0")
print("Wynik:\n" +
      nazwa1 + ": " + str(zwyciestwa1) + "\n" +
      nazwa2 + ": " + str(zwyciestwa2) + "\n")
if zwyciestwa1 > zwyciestwa2:
    print("Wygrywa " + nazwa1 + "!")
elif zwyciestwa1 < zwyciestwa2:
    print("Wygrywa " + nazwa2 + "!")
else:
    print("Remis!")
