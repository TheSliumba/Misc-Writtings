'''
Prie kelio trikojis matuoja speed
Greitis:
1) iki 50 ok
2) 51-59 warning
3) 60-70 fine
4) 70-130 warn cops
5) 130+ kill

1) Ekrane pateikti info, ką dayryt su vairuotoju
2) Parašyti tikrintojo funkciją, kuri gauna valstybinį numerį ir greitį,
    tada išspausdina atitinkamą veiksmą.
3) Parašyti dekoratorių, kuris aptikus 4 ar 5 atvejį viršijimo, praneštų artimiausiam
    ekipažui apie pažeidėją.
'''
def severe_response(f):
    def wrapper(data, police):
        for k,v in data.items():
            if v > 70:
                print(f'Calling police unit {min(police, key=lambda x:x[1])} to investigate vehicle {k}')
    return wrapper

@severe_response
def check_infraction(data, police):
    for k, v in data.items():
        if v < 50:
            print(f'{k} viskas ok')
        elif v > 50 and v <= 59:
            print(f'{k} warning')
        elif v > 60 and v <= 70:
            print(f'{k} bauda')
        elif v > 70 and v <= 130:
            print(f'{k} warn cops')
        else:
            print(f'Kill driver of {k}')

speeds = {'AAA111': 47, "BBB222": 55,"CCC333":65,'DDD444':84,"ZZZ666":170}
cops = {"Pirmas":10.5, "Antras":15}  # km nuo pažeidėjo
check_infraction(speeds,cops)