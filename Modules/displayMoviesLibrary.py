from Modules.importBase import *

def display_movies_library():
    print("\nWyświetlam Bibliotekę!\n")
    for movie in movies_library:
        print('------ Record no.: ', movie['id'], ' ------')
        print('Title: ', movie['Title'])
        print('Director: ', movie['Director'])
        print('Release: ', movie['Release'])
        print('Genres: ', end='')
        genresString = ""
        for genre in movie['Genres']:
              genresString += genre + ', '
        print(genresString[:-2])
        print('Rating: ', movie['Rating'], '\n')
    
movies_library = get_database()
