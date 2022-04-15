from Modules.verification import *
from Modules.importBase import *
import json

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

def add_movie(movie):
    if(check_movie(movie)):
        movies_library.append(movie)
        with open('./database/movies_library.json', "w", encoding="UTF-8") as file:
            json.dump(movies_library, file, ensure_ascii=False ,indent = 4)
        return movie

movies_library = get_database()
    
