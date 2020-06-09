def divisors(n, extremum= False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(n**0.5)+1):
        q, r = divmod(n, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(n//i)
    return sorted(divisors)

Examples:

divisors(15) # [3, 5]
divisors(15, True) # [1, 3, 5, 15]
