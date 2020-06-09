def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb%2 == 0:
        return False
    for i in range(3, int(nb**0.5)+1, 2):
        if nb%i == 0:
            return False
    return True

# Examples:

is_prime(13) # True
is_prime(14) # False
