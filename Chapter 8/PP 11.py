buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
while True:
    print('----Menu----')
    print('a. Tambah data buah')
    print('b. Beli buah')
    menu = input('Pilihan menu:')
    print('')

    if menu == 'A' or menu == 'a':
        print('Tambah Data Buah')
        tambah = input('Masukkan nama buah: ')
        if tambah in buah:
            print('Buah ini dahh ada bosss')
        else:
            harga = int(input('Harga buah: '))
            buah[tambah] = harga
            print('Data buah: ')
            for x,y in buah.items():
                print('-',x,'(Harga Rp.'+str(y)+')')    
            print('')
            True
        
    elif menu == 'B' or menu == 'b':
        print('Pilihan Buah')
        print(buah)
        totalharga = 0
        try:
            while True:  
                beli = input('Buah yang dibeli: ')
                if beli in buah:
                    berat = int(input('Berapa Kg       : '))
                    cek = input('Beli buah lain(yes/no)? ')
                    total = berat * buah[beli]
                    totalharga += total
                    if cek == 'yes' or cek == 'Yes':
                        True
                    elif cek == 'no' or cek == 'No':
                        print('----------------------------')
                        print('Total harga     :',totalharga)
                        print('')
                        break
                    else:
                        print('Pilihan ndak ada ogh')
                        break
                else:
                    print('Buah nggak ada niehhh')           
        except ValueError:
            print('Buah 404 Not Found')
        
    else:
        print('Pilihan nggak ada niehhh')