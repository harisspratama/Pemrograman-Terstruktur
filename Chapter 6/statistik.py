def sum(*n):
    jumlah = 0
    for i in n:
        jumlah += i
    return jumlah

def rata(*n):
    hitung = 0
    for i in n:
        hitung += 1
        rata = sum(*n) / hitung
    return rata

def maksimal(*n):
    max = n[0]
    for i in n:
        if (i > max):
            max = i
    return max

def minimal(*n):
    min = n[0]
    for i in n:
        if (i < min):
            min = i
    return min