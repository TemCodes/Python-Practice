def palin(x):
    x = x.strip().lower()
    k = len(x)-1
    for i in range(0,k):
        if(x[i] != x[k]):
            return False
        k-=1
    return True


print(palin('racecar'))
