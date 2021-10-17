print("***Status Kelulusan Mahasiswa***")
Nama= (input("Nama : "))
MTK= int(input("Nilai Matematika : ")) 
BHSINDO= int(input("Nilai Bahasa Indonesia :"))
IPA= int(input("Nilai IPA :"))
if(MTK<0) or (BHSINDO<0) or (IPA<0) or (MTK>100) or (BHSINDO>100) or (IPA>100):
    print("Maaf input ada yang tidak valid")
elif(MTK>70) and (BHSINDO>=60) and (IPA>=60):
    print("Status Kelulusan : ", Nama,"DINYATAKAN LULUS")
else:
    print("Status Kelulusan : ", Nama,"DINYATAKAN TIDAK LULUS")
