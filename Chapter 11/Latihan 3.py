import pathlib
import datetime
path = current_dir = str(pathlib.Path(__file__).parent)
openfile = open(path + '/Data minjam.txt','r')
peminjam1  = []
peminjam2 = []
peminjam3 = []
peminjam4 = []
peminjam5 = []
for line in openfile:
    spl = line.split("|")
    peminjam1.append(spl[0])
    peminjam2.append(spl[1])
    peminjam3.append(spl[2])
    peminjam4.append(spl[3])
    peminjam5.append(spl[4].strip())
pilihan = str(input("Masukkin kode membernya gan : "))
if pilihan in peminjam1:
    cari = True
    a = peminjam1.index(pilihan)
    sekarang = datetime.datetime.now()
    x = peminjam5[a]
    from datetime import datetime
    x = datetime.strptime(x, "%Y-%m-%d")
    rumus = x - sekarang
    from datetime import *
    pengembalian = datetime.date(sekarang)
    maksimal = datetime.date(x)
else:
    print("Data nggak ada niehh")
    exit()
if cari == True:
    rumus = datetime.date(sekarang) - maksimal
    rumus = int(rumus.days)
    bayardenda = 0
    if rumus >= 0:
        bayardenda = 2000 *(rumus)
        rumus = abs(rumus)
    elif rumus <= 0:
        rumus = 0
    print('='*60)
    print('Data Peminjaman Buku')
    print('='*60)
    print('Kode Member                    : ',peminjam1[a])
    print('Nama Member                    : ',peminjam2[a])
    print('Judul Buku                     :',peminjam3[a])
    print('Tanggal Mulai Peminjaman       : ',peminjam4[a])
    print('Tanggal Maks Peminjaman        : ',peminjam5[a])
    print('Tanggal Pengembalian           : ',pengembalian)
    print('Terlambat                      : ', rumus, 'Hari')
    print('Total denda                    :  Rp.',bayardenda)
    print('='*60)
else:
    print("Data tidak ditemukan dong")