buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
beli = input('Buah yang dibeli: ')
if beli in buah:
    try:
        berat = int(input('Berapa Kilogram nihh       : '))
        total = berat * buah[beli]
        print('**********************')
        print('Total harga     :',total)
    except ValueError:
        print('Gak bener nihh yang kamu masukin')   
else:
    print('Buahh Not Found 404 :)))')