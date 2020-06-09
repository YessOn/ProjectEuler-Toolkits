def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False
    
# Examples:

is_palindrome(101) # True
is_palindrome(147) # False
