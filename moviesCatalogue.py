from Modules.addMovie import *
from Modules.displayMoviesLibrary import *
from Modules.commandPrompt import *

print ("Witaj w Bibliotece Filmowej!")
cp_main_help()

wybor = ""

while wybor != 4:
    wybor = input("Wybór: ")
    if wybor == 'help':
        cp_main_help()
    else:
        try:
            wybor = int(wybor)
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
            print('\nWybór musi być liczbą lub poleceniem help\n')
        except KeyboardInterrupt:
            print('\nDziękujemy za skorzystanie z naszych usług! Do zobaczenia.\n')
            break
