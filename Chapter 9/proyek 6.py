nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('='*69)
print('NIM'.ljust(8),'Nama'.ljust(16),'MID'.ljust(8),'UAS'.ljust(8),'NILAI AKHIR'.ljust(16),'STATUS')
print('-'*69)
for isi in nilai:
    NilaiAkhir= (isi['mid'] + 2*isi['uas'])/3
    bulat=round(NilaiAkhir,2)
    if (NilaiAkhir>=60):
        status= 'LULUS'
    print(isi['nim'].ljust(8),isi['nama'].ljust(16),str(isi['mid']).ljust(8),str(isi['uas']).ljust(8),str(bulat).ljust(16), status)
print('='*65)