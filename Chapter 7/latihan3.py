print('*****************************')
print('KALKULATOR RATA - RATA')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

lagi = 'y'
count = 0
total = 0
while lagi == 'y':
    try:
        bil = int(input("Masukkan file kamu disini : "))
        total += bil
        count += 1
        lagi = input("Lagi gak say (y/n)?")
    except ValueError:
        print("Bukan bilangan bulat ini mahh")

if(count != 0):
    print('\nRata-ratanya niehh sayyy', total/count)
else:
    print('\ndata tidak ada/ salah')