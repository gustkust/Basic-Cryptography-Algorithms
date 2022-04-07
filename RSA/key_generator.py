from random import choice, randint



def sieve_of_eratosthenes(n = 10000):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):         
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    primes = []
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes
 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m


def generate_keys():
    primes = sieve_of_eratosthenes()

    p = choice(primes)
    while p > 100:
        p = choice(primes)

    q = choice(primes)
    while q > 100:
        q = choice(primes)

    n = p * q

    phi = (p - 1) * (q - 1)

    e = choice(primes)
    while gcd(phi, e) != 1:
        e = choice(primes)

    # to jest to samo co d = e^(-1) % phi, modular inverse
    d = pow(e, -1, phi)
    # d = modinv(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key
