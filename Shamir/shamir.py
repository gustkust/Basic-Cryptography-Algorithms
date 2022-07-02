from random import randint


def get_shares(secret, n=5, k=10000, t=3):
    if k - 1 < secret or secret < 0:
        print("Secret must be between 0 and k - 1")
    # udzialy
    si = []
    for i in range(n - 1):
        si.append(randint(1, k - 1))
    si.append(sum(si) % k)

    # 1
    p = randint(1000, 10000)
    # p = 1523

    # 2
    # t to liczba fragmentów potrzebna do odtworzenia
    a = [randint(0, p - 1) for i in range(t)]
    # a = [352, 62]

    # 3
    res = []
    for i in range(1, n + 1):
        res.append((i, (secret + sum([a[j - 1] * i ** j for j in range(1, t)])) % p))
    return res, p


def get_secret(shares, p):
    print(shares)
    res = 0
    for i, share_i in enumerate(shares):
        xi, yi = share_i
        l0 = 1
        for j, share_j in enumerate(shares):
            xj = share_j[0]
            if i != j:
                l0 *= xj / (xj - xi)
        res += l0 * yi
    return res % p


x, p = get_shares(954)
print(x)
print(get_secret(x, p))
print()
