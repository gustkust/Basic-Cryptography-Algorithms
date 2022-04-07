from random import randint
import tests


def prime_check(number):
    if number == 1 or number == 2 or number == 3:
        return True
    if number < 1 or number == 4 or (number - 3) % 4 != 0:
        return False
    div = 3
    while number > div:
        if number % div == 0:
            return False
        else:
            div += 1
    return True


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def bbs(p, q, amount=20000):
    # 1
    if p == q:
        print("p musi być różne od q")
        return 0
    if not prime_check(p):
        print("nieprawidłowa wartość p")
        return 0
    if not prime_check(q):
        print("nieprawidłowa wartość q")
        return 0
    n = p * q

    # 2
    x = 0
    while gcd(n, x) != 1 and x < 1:
        x = randint(1, n - 1)

    # 3
    x0 = x**2 % n

    # 4
    bits = []
    for i in range(amount):
        x0 = x0**2 % n
        if x0 % 2 == 0:
            bits.append(0)
        else:
            bits.append(1)
    return bits


res = bbs(7103, 5527)
# print(tests.frequency_test(res))
# print(tests.series_test(res))
# print(tests.poker_test(res))

if tests.frequency_test(res) and tests.series_test(res) and tests.poker_test(res):
    print("\nCorrect result")
else:
    print("\nWrong result")
