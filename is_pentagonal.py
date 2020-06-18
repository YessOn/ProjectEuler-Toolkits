def is_pentagonal(n):
    pen_test = ((1 + 24 * n)**0.5 + 1)/6
    return pen_test == int(pen_test)
