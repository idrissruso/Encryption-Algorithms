import random


def to_string(letters_list: list) -> str:
    return "".join(letters_list)


def make_key(n: int) -> list[int]:
    key = random.sample(range(1, n + 1), n)
    print(key)
    return key


def add_char(n: int, word: str, char: str) -> str:
    dif = len(word) % n
    if dif != 0:
        for i in range(n - dif):
            word = word + char
    return word


anahtar = make_key(5)


def encode(n: int, word: str) -> str:
    word_ = add_char(n=n, word=word, char="z")
    encoded_w = []
    i = 0
    while i < len(word_):
        for j in range(n):
            index = anahtar[j] - 1
            letter = word_[i + index]
            encoded_w.append(letter)
        i += n
    return to_string(encoded_w)


def decode(n: int, encoded_word: str) -> str:
    decoded_w = []
    i = 0
    while i < len(encoded_word):
        for j in range(n):
            index = anahtar.index(j + 1)
            letter = encoded_word[i + index]
            decoded_w.append(letter)
        i += n
    decoded_word = to_string(decoded_w)
    return decoded_word


print(encode(5, "naitwa idrissa rusongeka"))
print(decode(5, encode(5, "naitwa idrissa rusongeka")))
