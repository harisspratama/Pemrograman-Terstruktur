def starFormation1(n):
    colom = 1
    x = 0
    while(x < n):
        y = 0
        while(y < colom):
            print('* ', end='')
            y += 1
        colom += 1
        print('')
        x += 1

def starFormation2(n):
    colom = n
    x = 0
    while(x < n):
        y = 0
        while(y < colom):
            print('* ', end='')
            y += 1
        colom -= 1
        print('')
        x += 1

def starFormation3(n):
    if(n % 2 == 0): 
        # Untuk Genap
        starFormation1(n//2)
    else:
        # Untuk Ganjil
        starFormation1(n//2 + 1)
    starFormation2(n//2)
    
    
starFormation1(4)
starFormation2(4)
starFormation3(7)