try:
    namaFile = input("Masukkan file kamu disini: ")

    file = open(namaFile, "r")

    print('Isi dari file', namaFile, 'adalah:\n')
    print(file.read())

except FileNotFoundError:
    print('Maaf sayang gak ketemuu nihhh , coba cari di hatiku saja :))))')
