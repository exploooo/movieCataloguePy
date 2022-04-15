from importBase import *

def find_record_to_deletion(record_id):
    for movie in movies_library:
        if record_id == movie['id']:
            return movies_library.index(movie)
        else:
            print('Nie udało się znaleźć elementu o podanym ID w bazie danych')
            return 'err'

def remove_record(record_id):
    toDeletion = find_record_to_deletion(record_id)
    if toDeletion != 'err':
        del movies_library[toDeletion]

movies_library = get_database()
