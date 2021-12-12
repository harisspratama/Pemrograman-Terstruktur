import pathlib
path = current_dir = str(pathlib.Path(__file__).parent)
openfile = open(path + '/Biodata.txt','r')
bukafile= openfile.readlines()
File = len(bukafile)
dictionary = {}
x=0
for data in range(0,File) :
        a = bukafile[x]
        splitdata = a.split('|')
        nim = splitdata[0]
        nama = splitdata[1]
        alamat = splitdata[2].replace('\n', '')
        x+=1
        format1 = {'NIM':nim,'Nama':nama,'Alamat':alamat}
        format2 = {x : format1}
        dictionary.update(format2)
print(dictionary)