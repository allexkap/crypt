from itertools import cycle

chr_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ord_ru = {c: i for i, c in enumerate(chr_ru)}


def vigenere(text: str, key: str, de: bool = False) -> str:
    sign = -1 if de else 1
    return ''.join(
        chr_ru[(ord_ru[m] + ord_ru[k] * sign) % len(chr_ru)]
        for m, k in zip(text, cycle(key))
    )


print(vigenere('самосборка', 'задел'))
print(vigenere('щаруцшуцпл', 'задел', de=True))
