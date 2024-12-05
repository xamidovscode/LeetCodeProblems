import math

def pollard(n):
    def f(x, n):
        return (x * x + 1) % n

    x = 2
    y = 2
    d = 1
    while d == 1:
        x = f(x, n)
        y = f(f(y, n), n)
        d = math.gcd(abs(x - y), n)
        if d != 1 and d != n:
            return d
    return None

def find_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    factor = pollard(n)
    while factor is not None and factor != n:
        factors.append(factor)
        n //= factor
        factor = pollard(n)
    if n > 1:
        factors.append(n)
    return factors

N = 7571
factors = find_factors(N)
print("Ko‘paytuvchilar:", factors)
