from Modules.verification import *
from Modules.importBase import *
import json


# Getting lowest free id from database to assign it to new movie record
def get_lowest_free_id(database):
    idies = [
        int(movie['id'])
        for movie in database
    ]
    idies.sort()
    for i in range (min(idies), max(idies)+1):
        if i not in idies:
            return i    
    return max(idies)+1


# Questionary that gets data from user and parses it into a new movie object
def movie_add_questionary():
    title = check_string_data(input("Title: "))
    while title == 'err':
        title = check_string_data(input("Title: "))
    director = check_string_data(input("Director: "))
    while director == 'err':
        director = check_string_data(input("Director: "))
    release = check_date(input("Release Date (yyyy-mm-dd): "))
    while release == 'err':
        release = check_date(input("Release Date (yyyy-mm-dd): "))
    genres = check_string_data(tuple(map(str, input("Generes (split with ','): ").split(', '))))
    while genres == 'err':
        genres = check_string_data(tuple(map(str, input("Generes (split with ','): ").split(', '))))
    rating = check_rating(input("Rating: "))
    while rating == 'err':
        rating = check_rating(input("Rating: "))

    movie = {
             "id": get_lowest_free_id(movies_library),
             "Title": title,
             "Director": director,
             "Release": release,
             "Genres": genres,
             "Rating": rating,
             "Verified": False
        }
    
    return movie

# function that inserts new movie record into database

def insert_movie_to_database(movie):
    if(check_movie(movie)):
        movies_library.append(movie)
        with open('./database/movies_library.json', "w", encoding="UTF-8") as file:
            json.dump(movies_library, file, ensure_ascii=False ,indent = 4)
        return movie
    else:
        return 'err'

# main function called in main menu - calls questionary and gives feedback whether movie was added or not

def movie_add():
    print("\nDodawanie Filmu\n")
    try:
        movie = insert_movie_to_database(movie_add_questionary())
        print('\nRekord został wprowadzony do bazy i oczekuje na weryfikację!\n')
    except:
        print('\nPrzerwano operację wprowadzania filmu!\n')

movies_library = get_database()
    
