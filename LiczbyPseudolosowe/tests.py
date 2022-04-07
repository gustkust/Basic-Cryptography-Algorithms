def frequency_test(bits):
    print("number of zeros:", 20000 - sum(bits))
    print("number of ones:",  sum(bits))
    if 9725 < sum(bits) < 10275:
        return True
    return False


def series_test(bits):
    series = [
        {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0},
        {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0},
    ]
    length = len(bits)
    index = 1
    cur_series = 1
    while index < length:
        if bits[index - 1] != bits[index]:
            if cur_series < 6:
                series[bits[index - 1]][cur_series] += 1
            else:
                series[bits[index - 1]][6] += 1
            cur_series = 1
        else:
            cur_series += 1
        if cur_series > 25:
            return False
        index += 1
    for i in series:
        if (
            2315 < i[1] < 2685
            and 1114 < i[2] < 1386
            and 527 < i[3] < 723
            and 240 < i[4] < 384
            and 103 < i[5] < 209
            and 103 < i[6] < 209
        ):
            pass
        else:
            return False
    print("series of zeros:", series[0])
    print("series of ones:", series[1])
    print("longest series shorter than 26")
    return True


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


def poker_test(bits):
    bits = list(split(bits, int(len(bits)/4)))
    amount = [0] * 16
    for part in bits:
        amount[part[0] * 8 + part[1] * 4 + part[2] * 2 + part[3] * 1] += 1
    print("poker test result:", 16/5000 * sum([i**2 for i in amount]) - 5000)
    if 2.16 < 16/5000 * sum([i**2 for i in amount]) - 5000 < 46.17:
        return True
    return False
