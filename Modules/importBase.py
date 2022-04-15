import json

def change_to_tuple(movie):
    movie['Genres'] = tuple(movie['Genres'])

def change_generes_type(movies):
    for movie in movies:
        change_to_tuple(movie)
    return movies

def get_database():
    with open('./database/movies_library.json', encoding="UTF-8") as file:
        movies_library = json.load(file)
    change_generes_type(movies_library)
    return movies_library

    
