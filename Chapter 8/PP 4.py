sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print(sayur)
def menu():
    print('Menu:')
    print('1. Tambah dong sayurnys biar sehat')
    print('2. Hapus sayur yang kamu mau hapus :(')
    print('3. Tampilkan sayur yang ada ')
    print('4. Exit')
    pilih = input('Pilih yang mana hayoo = ')
    if pilih == '1':
        print('++Tambah list sayur++')
        tambah = input('Tambah sayur= ')
        sayur.append(tambah)
        menu()
    elif pilih == '2':
        try:
            print('--Hapus list sayur--')
            hapus = input('Hapus sayur= ')
            sayur.remove(hapus)
            menu()
        except ValueError:
            print('Wahh nggak ketemu niehh , kamu gimana siehh')
            print('')
            menu()
    elif pilih == '3':
        print('##Data sayur##')
        print(sayur)
        print('')
        menu()
    elif pilih == '4':
        quit()
    else:
        print('Sayur Not Found 404 ')
        print('')
        menu()
menu()