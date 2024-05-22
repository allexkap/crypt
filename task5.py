def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    k, a = divmod(a, b)
    d, y, x = exgcd(b, a)
    return d, x, y - k * x


def rsa_encrypt(p, q, e, text):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = exgcd(e, phi)[1]
    data = tuple(ord(ch) - 848 for ch in text)
    print(d, n)
    print(''.join(f'{i}' for i in data))
    print(''.join(f'{pow(i, e, n):04}' for i in data))


def rsa_decrypt(data, public_key, private_key):
    n = public_key[1]
    d = private_key[0]
    print(
        ''.join(
            chr(pow(int(data[p * 4 : (p + 1) * 4]), d, n) + 848)
            for p in range(len(data) // 4)
        )
    )


if __name__ == '__main__':
    rsa_encrypt(
        p=193,
        q=23,
        e=1847,
        text='Гуггенхайм',
    )
    rsa_decrypt(
        data='569644650331249058481576',
        public_key=(1483, 6499),
        private_key=(3811, 6499),
    )
