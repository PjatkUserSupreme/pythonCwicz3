liczby = input("Podaj liczby przedzielone przecinkami: ")

lista_liczb = liczby.split(",")
ilosc = 0
suma = 0
min = 0
max = 0
for index in range(0, len(lista_liczb)):
    ilosc += 1
    suma += int(lista_liczb[index])
    if min > int(lista_liczb[index]):
        min = int(lista_liczb[index])
    if max < int(lista_liczb[index]):
        max = int(lista_liczb[index])


print("Ilosc liczb: " + str(ilosc))
print("Suma liczb: " + str(suma))
print("Najmniejsza liczba: " + str(min))
print("Najwieksza liczba: " + str(max))
