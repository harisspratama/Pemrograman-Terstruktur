def formasiA(n):
    for star in range (0,n):
        formasi = '*' *(1+(star-2)*2)
        print(formasi.center(1+2*n))
def formasiB(n):
    for star in range (0,n):
        formasi = '*' *(n+(star-1)*-2)
        print(formasi.center(1+2*n))        
def formasiC(n):
        formasiA(n)
        formasiB(n)
while True:
    jumlah=int(input('Masukkan jumlah baris yang kamu inginkan sobat : '))
    if (jumlah%2==1):
        formasiC(jumlah)
        break
    else:
        print('Maaf sobat bilanganmu tidak ganjil :( ')
        lagi=input('Dimasukkin lagi nggak niehhh(Yes/No)? ')
        if(lagi=='Yes'): 
            continue
        else:
            break