import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
file = open(path + '/Angka.txt','r')
Ganjil = 0
Genap  = 0
for data in file:
    try:
        if(int(data) % 2 == 0):
            Ganjil += 1
        else:
            Genap += 1
    except:
        print(data.rstrip("\n") ," : Bukan angka nihh sayang")
print("Banyak Jumlah Bilangan Genap nihhh  :",Genap)
print("Banyak Jumlah Bilangan Ganjil niehhh :",Ganjil)
