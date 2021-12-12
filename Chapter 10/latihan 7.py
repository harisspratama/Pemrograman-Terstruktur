import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
openfile = open(path + '/hasil sandi.txt','r')
dekripsi= openfile.readline()
buatlist = list(dekripsi) 
n = int(input('Masukkan jumlah pergeserannya dong = '))
dekripsisandicaesar = ''
for huruf in buatlist:
    if (huruf.isalpha()):
        ascii= ord(huruf)
        caesar = 65 + ((ascii % 65)- n)%26
        dekripsisandicaesar += chr(caesar)
    else : 
        dekripsisandicaesar += ' '
print('Hasil ke semula            = ', dekripsisandicaesar)
openfile = open(path + '/dekripsiSandi.txt','w')
openfile.write(dekripsisandicaesar)
openfile.close