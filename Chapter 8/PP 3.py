try:
    data = []

    mhs = int(input('Berapa banyak nama mahasiswa yang ingin kamu masukkan say ?: '))
    for i in range(mhs):
        nama = input('Masukkan namanya dong : ')
        data.append(nama)
 
    for nama in data:
        print(nama, '('+ str(len(nama)) +'karakter)')
except ValueError:
    print(' Nggak Valid woyyy , ayo fokus dong cari yang bener !!! ')