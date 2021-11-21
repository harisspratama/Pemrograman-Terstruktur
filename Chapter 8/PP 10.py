buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
print(buah)
totalharga = 0
try:
    while True:  
        beli = input('Buah yang kamu beli : ')
        if beli in buah:
            berat = int(input('Berapa Kilogram nihh : '))
            cek = input('Beli buah lain(yes or no)? ')
            total = berat * buah[beli]
            totalharga += total
            if cek == 'yes' or cek == 'Yes':
                True
            elif cek == 'no' or cek == 'No':
                print('----------------------------')
                print('Total harga     :',totalharga)
                break
            else:
                print('Pilihan nggak ada , ayo cari yang lain !!!')
                break
        else:
            print('Buahnya gaada nihh cari yang bener dongg !!!')
except ValueError:
    print('Buah 404 Not Found')