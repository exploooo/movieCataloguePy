from Modules.addMovie import *

try:
    film = add_movie(movie_add_questionary())
    print('Rekord został wprowadzony do bazy i oczekuje na weryfikację!')
except:
    print('Przerwano operację wprowadzania filmu!')
