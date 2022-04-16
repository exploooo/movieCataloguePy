from Modules.importBase import *
from Modules.removeMovie import *

def display_movies_library():
    movies_library = get_database()
    print("\nWyświetlam Bibliotekę!\n")
    ended_at = display_next(5, 0)
    print("""Next *n* - wyświetlanie następnych n pozycji
Show *id* - displays more info about specific movie
Quit - exit
""")
    command = True
    while command:
        try:
            command = input('Wybór(Wyświetlanie-Biblioteki): ').lower()
            if command[0:4].lower().replace(' ', '') == 'next':
                try:
                    quantity = int(command[5:].replace(' ', ''))
                    display_next(quantity, ended_at)
                except TypeError:
                    print('\nPodano błędną wartość, dla komendy next należy podać ilość elementów do wyświetlenia\n')
            elif command[0:4].replace(' ', '').lower() == 'show':
                try:
                    record_id = int(command[5:].replace(' ', ''))
                    show_record_details(record_id, movies_library)
                except:
                    print('\nPodano błędną wartość, dla komendy show należy podać ilość elementów do wyświetlenia\n')
            elif command == 'q' or command == 'quit':
                break
            else:
                print('\nNie rozpoznano komendy\n')
        except KeyboardInterrupt:
            command = 'q'

def display_next(quantity, beggining):
    movies_library = get_database()
    last_id = movies_library[-1]['id']
    previous_id = beggining
    i = 1
    while i <= quantity:
        if previous_id == last_id:
            print("\nWyświetliłem już wszystkie filmy w naszej bibliotece!\nJeśli nie znalazłeś tytułu, który cię interesuje zajrzyj ponownie później lub dodaj go do bazy.\n")
            break
        try:
            print('------ Record no.: ', movies_library[previous_id]['id'], ' ------\n')
            print('Title: ', movies_library[previous_id]['Title'])
            print('Director: ', movies_library[previous_id]['Director'])
            print('Release: ', movies_library[previous_id]['Release'])
            print('Genres: ', end='')
            genresString = ""
            for genre in movies_library[previous_id]['Genres']:
                genresString += genre + ', '
            print(genresString[:-2])
            print('Rating: ', movies_library[previous_id]['Rating'])
            if movies_library[previous_id]['Verified']:
                s = '\u2713'
            else:
                s = '\u2715'
            s.encode('utf8')
            print('Verified:', s, '\n')
            previous_id+=1
            i+=1
        except IndexError:
            print('chuj')
            previous_id+=1
    return previous_id

def show_record_details(record_id, database):
    record_index = find_record_of(record_id)
    try:
        print('\n',database[record_index]['Title'],'\n')
    except TypeError:
        return


