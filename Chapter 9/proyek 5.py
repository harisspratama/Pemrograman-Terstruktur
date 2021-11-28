nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
print('='*69)
print('NIM'.ljust(8),'Nama'.ljust(16),'N MID'.ljust(8),'N UAS')
print('-'*69)
for isi in nilai:
    print(isi['nim'].ljust(8),isi['nama'].ljust(16),str(isi['mid']).ljust(8),str(isi['uas']))
print('='*69)