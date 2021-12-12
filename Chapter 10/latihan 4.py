import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
openfile = open(path + '/Biodata.txt','r')
biodata1 = []
biodata2 = []
biodata3 = []
for data in openfile:
    spl = data.split('|')
    biodata1.append(spl[0])
    biodata2.append(spl[1])
    biodata3.append(spl[2].strip())
print('Program mencari data mahasiswa')
print('-'*50)
inputNIM = str(input('Masukkan NIM yang mau dicari nihh : '))
print('-'*50)
if inputNIM in biodata1:
    a = biodata1.index(inputNIM)
    print('Data Mahasiswa:')
    print('NIM	: ',biodata1[a])
    print('Nama	: ',biodata2[a])
    print('Alamat	: ',biodata3[a])
else:
    print("Datanya gaada niehhhh")
print('-'*50)