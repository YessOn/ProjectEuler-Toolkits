def generate_pentagons(n_of_pentagons):
    pentagons = (num * (3 * num - 1) // 2 for num in range(1, n_of_pentagons))
    for _ in range(n_of_pentagons - 1):
        yield next(pentagons)
