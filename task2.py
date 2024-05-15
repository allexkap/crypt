def feistel_round(data: str, subkey: str) -> str:
    h = len(data) // 2
    l, r = data[:h], data[h:]
    return r + f'{int(l, 2) ^ int(r, 2) ^ int(subkey, 2):0>{h}b}'


m = '00001100101111000101'
for k in ('0110011011', '0111011001'):
    m = feistel_round(m, k)
print(m)
