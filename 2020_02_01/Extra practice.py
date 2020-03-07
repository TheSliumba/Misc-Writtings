'''
stock = {"bike":40, "scooter":10}
prices = {"bike":120, "scooter":40}

Paskaičiuot sandėlio liktuį pinigais.
1)Sukurti naują dictionary kuriame bus prekė ir viso likučio vertė pinigais.
2)Perkelti skaičiavimą į f-ją
3)Parašyti funkiją, kuri atspausdina likučių sumą.
4)Likučių sumos f-ją paversti į dekoratorių
'''
def totals(f):
    def wrapper(inv, kain):
        rem = f(inv,kain)
        totals = 0
        for i in rem.values():
            totals += i
        return f'Final sum is {totals}'
    return wrapper

def rep(f):
    def wrapper(inv,kain):
        rem = f(inv,kain)
        for k,v in rem.items():
            print(f'Item: {k}, Price: {v}')
    return wrapper


@rep
def calculate_value_remainder(stock, prices):
    remainder={}
    for k, v in stock.items():
        if k in remainder:
            remainder[k] += stock[k] * prices[k]
        else:
            remainder[k] = stock[k] * prices[k]
    return remainder

'''def total(remainder):
    totals = 0
    for i in remainder.values():
        totals += i
    return totals'''

stock = {"bike":40, "scooter":10}
prices = {"bike":120, "scooter":40}

print(calculate_value_remainder(stock,prices))
#print(total(calculate_value_remainder(stock,prices)))