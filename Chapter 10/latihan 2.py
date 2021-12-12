import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
data = ''
while True: 
    openfile = open(path + '/Biodata.txt','a')
    nim = input('Masukkan NIM nya dong :')
    nama =input('Masukkan Nama nya dong :')
    alamat =input('Masukkan Alamat nya dong :')
    formatdata= nim + '|' + nama + '|' + alamat + '\n'
    Repeat =input('Mau masukiin data lagi gak niehh ? yes/no :')
    if (Repeat=='yes'):
        openfile.write(formatdata)
        openfile.close
        continue
    elif (Repeat=='no'):
        openfile.write(formatdata)
        openfile.close
        break