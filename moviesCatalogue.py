from Modules.addMovie import *
from Modules.displayMoviesLibrary import *

print ("""Witaj w Bibliotece Filmowej!

Aby wyświetlić bibliotekę filmową wybierz: 1
Aby dodać film wybierz: 2
Aby się zalogować lub założyć konto wybierz: 3
Aby zweryfikować dodane ostatnio rekordy wybierz: 4
Aby zakończyć działanie programu wybierz: 5
""")

wybor = ""

while wybor != 5:
    try:
        wybor = int(input("Wybor: "))
        match wybor:
            case 1:
                display_movies_library()
            case 2:
                movie_add()
            case 3:
                print("\nZaloguj się/Utwórz konto\n")
            case 4:
                print("\nDziękujemy za skorzystanie z naszych usług! Do zobaczenia.\n")
            case wybor if wybor > 5 or wybor < 0:
                print("\nDla podanego numeru nie ma operacji!\n")
    except ValueError:
        print('\nWybór musi być liczbą!\n')
    except KeyboardInterrupt:
        print('\nDziękujemy za skorzystanie z naszych usług! Do zobaczenia.\n')
        break
