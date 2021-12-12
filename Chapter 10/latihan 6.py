import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
text = 'MAWAR ITU MERAH VIOLET ITU BIRUU , AKU INGIN KE KAMAR MANDI'
buatlist = list(text)
print('Program Pembuat Sandi')
print(text)
n = int(input('Masukkan jumlah pergeserannya dong = '))
sandicaesar = ''
for huruf in buatlist:
    if (huruf.isalpha()):
        ascii= ord(huruf)
        caesar = 65 + ((ascii % 65)+ n)%26
        sandicaesar += chr(caesar)
    else : 
        sandicaesar += ' '
print('Hasil penyandian            = ', sandicaesar)
openfile = open(path + '/hasil sandi.txt','w')
openfile.write(sandicaesar)
openfile.close