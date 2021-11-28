def star(n):
    for x in range(1,n):
        bintang = "*" * (1 +(x-1)*2)
        print(bintang.center(1+2*n))
star(5)