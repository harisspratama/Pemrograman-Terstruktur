buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
while True:
    print('----Menu----')
    print('a. Tambah data buah')
    print('b. Hapus data buah')
    print('c. Beli buah')
    menu = input('Pilihan menu: ')
    print('')

    if menu == 'A' or menu == 'a':
        print('-Tambah Data Buah-')
        tambah = input('Masukkan nama buah: ')
        if tambah in buah:
            print('Buah ini sudah tersedia')
        else:
            harga = int(input('Harga buah: '))
            buah[tambah] = harga
            print('Data buah: ')
            for x,y in buah.items():
                print('-',x,'(Harga Rp.'+str(y)+')')    
            print('')
            True
            
    elif menu == 'B' or menu == 'b':
        print('-Hapus Data Buah-')
        hapus = input('Masukkan nama buah: ')
        if hapus in buah:
            del buah[hapus]
            True
        else:
            print('Nama buah tidak ditemukan')
            
    elif menu == 'C' or menu == 'c':
        print('-Pilihan Buah-')
        print(buah)
        totharga = 0
        try:
            while True:  
                beli = input('Buah yang dibeli: ')
                if beli in buah:
                    berat = int(input('Berapa Kg       : '))
                    cek = input('Beli buah lain(y/n)? ')
                    total = berat * buah[beli]
                    totharga += total
                    if cek == 'y' or cek == 'Y':
                        True
                    elif cek == 'n' or cek == 'N':
                        print('----------------------------')
                        print('Total harga     :',totharga)
                        print('')
                        break
                    else:
                        print('Pilihan tidak tersedia')
                        break
                else:
                    print('Buah tidak tersedia')           
        except ValueError:
            print('input tidak valid')
        
    else:
        print('Pilihan tidak tersedia')