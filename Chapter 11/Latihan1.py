from datetime import *
try:
    def diffDate(x):
        sekarang = datetime.date(datetime.now())
        print('Hari ini tanggal: ', sekarang)
        splitt = x.split('-')
        x = date(year = int(splitt[0]), month = int(splitt[1]), day = int(splitt[2]))
        selisih = x - sekarang
        print(selisih.days)
        return
    tanggal = input('Masukkin format tanggalnya nihh (tahun-bulan-tanggal): ')
    diffDate (tanggal)
except ValueError:
    print('Sayang sekali format nya salah')
except IndexError:
    print('Sayang sekali format nya salah')
