import random

miasta = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

while len(miasta) > 0:
    index = random.randint(0, len(miasta) - 1)
    print(miasta.pop(index))

