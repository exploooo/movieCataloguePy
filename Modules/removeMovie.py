from Modules.importBase import *

def find_record_of(record_id):
    for movie in movies_library:
        if record_id == movie['id']:
            return movies_library.index(movie)
        else:
            print('\nNie udało się znaleźć elementu o podanym ID w bazie danych\n')
            return

def remove_record(record_id):
    toDeletion = find_record_of(record_id)
    if toDeletion:
        del movies_library[toDeletion]

movies_library = get_database()
