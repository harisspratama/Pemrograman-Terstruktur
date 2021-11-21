def mahal(x):
    maks = max(x.values())
    for x,y in x.items():
        if y == maks:
            return x
def rata2(x):
    rata = sum(x.values())/len(x)
    return rata
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
print(buah)
print('Termahal   :',mahal(buah))
print('Harga rata2:',rata2(buah))