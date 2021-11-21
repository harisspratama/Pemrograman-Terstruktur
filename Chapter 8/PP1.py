try:
    banyak = int(input('Berapa banyak angka yang mau dimasukkan nihh sayangku ? '))
    bil = []

    for i in range(banyak):
        angka = int(input('Masukkan angka yang ke-' + str(i+1) + ': '))
        bil = bil + [angka]

    bil.sort(reverse=True)
    print('Angka yang kamu masukkan ini nihhh', bil)

except ValueError:
    print('INI BUKAN ANGKA SAYANG , KAMU GIMANA SIEHHH!!')
