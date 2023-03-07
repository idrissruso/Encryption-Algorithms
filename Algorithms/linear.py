from utils import letters, to_string


def encode(word: str, a: int, b: int) -> str:
    encoded = []
    for letter in word:
        x = letters.index(letter)
        y = a * x + b
        index = y if y <= len(letters) else y % len(letters)
        encoded.append(letters[index])
    return to_string(encoded)


def decode(word: str, a: int, b: int) -> str:
    encoded = []
    for letter in word:
        x = letters.index(letter)
        y_ = int((x - b) / a)  # ters fonksiyon
        index = y_ if y_ <= len(letters) else y_ % len(letters)
        encoded.append(letters[index])
    return to_string(encoded)



