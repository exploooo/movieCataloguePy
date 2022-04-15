from Modules.importBase import *

def display_movies_library():
    print("\nWyświetlam Bibliotekę!\n")
    display_next(5)

def display_next(quantity):
    movies_library = get_database()
    for movie in movies_library:
        print('------ Record no.: ', movie['id'], ' ------\n')
        print('Title: ', movie['Title'])
        print('Director: ', movie['Director'])
        print('Release: ', movie['Release'])
        print('Genres: ', end='')
        genresString = ""
        for genre in movie['Genres']:
              genresString += genre + ', '
        print(genresString[:-2])
        print('Rating: ', movie['Rating'])
        if movie['Verified']:
            s = '\u2713'
        else:
            s = '\u2715'
        print('Verified:', s, '\n')
        
