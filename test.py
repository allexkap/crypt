from PIL import Image


def chr_ru(i: int) -> str:
    if i < 128:
        return chr(i)
    return chr(i + 848)


d, p, q = 8135, 97, 149

images = []
for path in ('./resources/array_int_parts_3.png', './resources/array_remainders_3.png'):
    images.append(list(Image.open(path).getdata()))
data = map(lambda x: x[0] * 256 + x[1], zip(*images))
print(''.join(chr_ru(pow(int(block), d, p * q)) for block in data))
