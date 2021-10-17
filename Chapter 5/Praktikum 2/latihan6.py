from random import randint
Angka = randint(0, 100)
Nilai=100
print ('Hallow.. My NAme is Mr. Pee , nah aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100 niehhh. Ayoo tebak kalo bisaa :)))!!!!!')
while True:
    menebak = int(input('Tebakan Kamu nichh : '))
    if menebak > Angka :
        print ('HUHUHUU bilangan Kamu terlalu besar dehhhh :(((')
    elif menebak < Angka :
        print ('XIXIXIXI bilangan Kamu kekecilan siehhh')
    elif menebak == Angka :
        print ('COOLLLL tebakan kamu benarrr :DDD, SELAMATT YAACHH :vvv')
        break
    Nilai-=2
    if Nilai==0 :
        print('Yaahhh nilai kamu sudah 0 niehhh , kamu nggak boleh main lagi niehhh :( , TETAP SEMANGAT YAAA !!! :333')
print('Nilai kamu nihh sayang :', Nilai)
    
