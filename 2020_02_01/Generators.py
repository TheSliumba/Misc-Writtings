'''
Parašyti generatoriaus funkciją, kuri gavusi list [a,b,c,d] grąžintų [A1,B2,C3,D4]
'''
def modify(f):
    def wrapper(raides):
        ce = f(raides)
        for item in ce:
            raide = item[0]
            skaicius = int(item[1:])
            yield f"{raide}{raide*skaicius}"
    return wrapper

@modify
def ca_enum(raides):
    for ind, raid in enumerate(raides,1):
        yield raid.upper()+str(ind)

ca = ca_enum(['a','b','c','d'])

for i in ca:
    print(i)