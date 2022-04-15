import re
from datetime import datetime

def check_date(date):
    #checking if date is parsed in correct format
    regex = r"[0-9]{4}\-[0-9]{1,2}\-[0-9]{1,2}"
    if re.match(regex, date):
        data = tuple(map(int, date.replace('-',', ').split(', ')))
        day = data[2]
        month = data[1]
        year = data[0]
        try:
            #Using datetime just to check if the date is correct
            data = datetime(year, month, day)
            return date
        except:
            print('Podano błędną datę')
            return 'err'
    else:
        print ('Podano błędny format daty, spróbuj użyć "-" zamiast kropek i zastosować się do formatu yyyy-mm-dd')
        return 'err'

# A function that checks if string data is correctly formated

def check_string_data(data):
    if type(data) == tuple:
        data_str = ""
        for record in data:
            data_str += str(record) + " "
        if len(data_str) > 64:
            print('Wpis jest za długi! Maksymalny rozmiar - 64 znaki')
            return 'err'
        return data
    else:
        if len(data) > 64:
             print('Wpis jest za długi! Maksymalny rozmiar - 64 znaki')
             return 'err'
        return data

# A function that checks if our rating data is higher than 0 and lower than 100

def check_rating(rating):
    try:
        rating = int(rating.replace(' ', ''))
    except:
        print("Print Podana wartość nie jest liczbą!")
        return 'err'
    if rating >= 0 and rating <= 100:
        return rating
    return 'err'
    

# A funcion that checks if is there any error in parsed data

def check_movie(movie):
    for key in movie:
        if movie[key] == 'err':
            return False
    return True
