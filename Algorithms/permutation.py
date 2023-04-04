import random


def make_key(n: int) -> list[int]:
    sayi = [i for i in range(n)]
    anahtar = random.sample(sayi, n)
    return anahtar


def add_char(n: int, word: str, char: str) -> str:
    dif = len(word) % n
    print(dif)
    if dif != 0:
        for i in range(dif):
            word = word + char
    return word

