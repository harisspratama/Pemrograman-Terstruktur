mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("=" * 69)
print("NIM".ljust(12),"NAMA MAHASISWA".ljust(24),"TGL LAHIR".ljust(18),"TEMPAT LAHIR".ljust(18))
print("-" * 69)
for data in mhs:
    dataList            = data.split(":")
    nim                 = dataList[0]
    nama                = dataList[1]   
    tanggalLahir        = dataList[2]
    dataTglLahir        = tanggalLahir.split('-')
    newFormatTglLahir   = "{0}/{1}/{2}".format(dataTglLahir[2],dataTglLahir[1],dataTglLahir[0])
    tempatLahir         = dataList[3]
    print(nim.ljust(12),nama.ljust(24),newFormatTglLahir.ljust(18),tempatLahir.ljust(18))
print("=" * 70)