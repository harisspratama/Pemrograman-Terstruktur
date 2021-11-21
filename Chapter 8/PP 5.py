def kuadrat(bil):
    x = []
    for data in bil:
        data = data ** 2
        x = x + [data]
    return x
bil = [3,4,5,6,8,10]
print('Kuadrat dari list', bil,'adalah',kuadrat(bil))
