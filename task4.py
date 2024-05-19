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


data = [1, 1, 0, 1, 0, 0]
poly = (6, 5, 3, 1)

print(*lfsr(data, poly))
