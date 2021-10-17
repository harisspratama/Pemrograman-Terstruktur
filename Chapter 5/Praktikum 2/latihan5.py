from random import randint
Angka = randint(0, 100)
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