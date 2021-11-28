import random
def shuffleString(x, n):
    List = []
    i = 0
    while i < n:
        acak = ''.join(random.sample(x,len(x)))
        if(acak not in List):
            List += [acak]
            i += 1
    print(List)
shuffleString('kamu',2)
shuffleString('kamu',3)
shuffleString('kamu',4)