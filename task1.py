from itertools import cycle


chr_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ord_ru = {c: i for i, c in enumerate(chr_ru)}


def Vigenere(msg, key, de=False):
    sign = -1 if de else 1
    return ''.join(
        chr_ru[(ord_ru[m] + ord_ru[k] * sign) % len(chr_ru)]
        for m, k in zip(msg, cycle(key))
    )


print(Vigenere('самосборка', 'задел'))
print(Vigenere('щаруцшуцпл', 'задел', de=True))
