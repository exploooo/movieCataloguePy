from Modules.addMovie import *

print ("""Witaj w Bibliotece Filmowej!

Aby wyświetlić bibliotekę filmową wybierz: 1
Aby dodać film wybierz: 2
Aby usunąć film wybierz: 3
Aby zweryfikować dodane ostatnio rekordy wybierz: 4
Aby zakończyć działanie programu wybierz: 5
""")

wybor = 1

while wybor != 5:
    try:
        wybor = int(input("Wybor: "))
        match wybor:
            case 1:
                print("Wyświetlam Bibliotekę!")
            case 2:
                print("Dodawanie Filmu")
            case 3:
                print("Usuwanie Filmu")
            case 4:
                print("Weryfikacja")
            case 5:
                print("Dziękujemy za skorzystanie z naszych usług! Do zobaczenia.")
            case wybor if wybor > 5 or wybor < 5:
                print("Dla podanego numeru nie ma operacji!")
    except ValueError:
        print('Wybór musi być liczbą!')
