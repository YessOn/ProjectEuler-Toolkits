def is_abundant(n):
    return sum(divisors(n))+1 > n

# Examples:

is_abundant(12) # True
is_abundant(15) # False
