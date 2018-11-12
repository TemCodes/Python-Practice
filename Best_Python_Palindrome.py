def palin(x):
    x = x.strip().lower()
    if x == x[::-1]:
        return True
    return False

print(palin('Racecar'))
