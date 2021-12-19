import datetime
import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
data = ''
while True:
    kode = input("Masukkin Kode Member  = ")
    nama = input("Masukkin Nama Member	= ")
    judul = input("Masukkin Judul Buku   = ")
    sekarang = datetime.date.today()
    tenggang = datetime.timedelta(days=7)
    pinjam = str(sekarang + tenggang)
    sekarang2 = str(sekarang)
    openfile = open(path + '/Data Peminjam.txt','a')
    openfile.write(kode + "|" + nama + "|" + judul + "|" + sekarang2 + "|" + pinjam + "\n")
    openfile.close
    Ulangi = input("Ulangin nggak ? (y/n) = ")
    if Ulangi == "n":
        openfile = open(path + '/Data minjam.txt','r')
        print("data peminjam :")
        print(openfile.read())
        openfile.close()
        break
    elif Ulangi == "y":
        continue
    else:
        print("input anda salah")
        exit()