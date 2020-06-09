def primes_below(end):
    if end < 2:
        return []
    lng = (end//2) - 1
    primes = [True]*lng
    for i in range(int(lng**0.5)):
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False
    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

# Examples :

primes_below(10) # [2, 3, 5, 7]
primes_below(40) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
