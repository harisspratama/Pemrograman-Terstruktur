def sortStringByChar(x):
    karakter = []
    for i in x:   
        hitung = len(i)
        karakter.append(hitung)
        x.sort(reverse=True)
    return x    
myData = ['Semongko','Srikaya','AnggurMerah']
print(sortStringByChar(myData))