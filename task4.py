from functools import reduce
from itertools import count


def lfsr(data, poly):
    data = data[::-1]
    state = data[:]
    output = []
    for i in count():
        state.append(reduce(lambda a, b: a ^ b, (state[i - 1] for i in poly if i > 1)))
        output.append(state.pop(0))
        if state == data:
            return i + 1, output[::-1]


def rc4(key, n, m):
    key_len = len(key)
    s = [i for i in range(n)]
    output = []

    j = 0
    for i in range(n):
        j = (j + s[i] + key[i % key_len]) % n
        s[i], s[j] = s[j], s[i]
    s0 = s.copy()

    j = 0
    for i in range(m):
        i = (i + 1) % n
        j = (j + s[i]) % n
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % n
        output.append(s[t])

    return s0, output[::-1]


data = [1, 1, 0, 1, 0, 0]
poly = (6, 5, 3, 1)
print(*lfsr(data, poly))

key = (7, 0, 9, 2, 4, 1, 3, 8, 5, 6)
print(*rc4(key, 10, 5))
