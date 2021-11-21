def datastat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    return(a,b,c)
data = []
banyak = int(input('Berapa banyak jumlah angka yang mau kamu masukkan niehh ?: '))
for i in range(banyak):
    angka = int(input('Masukkan angka yang kamu inginkan : '))
    data.append(angka)
print('rata2,max,min:',datastat(data))