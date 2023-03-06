from typing import List
from utils import to_string, letters


def shifted(letters_to_shift: List, shift: int) -> List[str]:
    shifted_list = []
    t_shift = shift if shift <= len(letters_to_shift) else shift - len(letters_to_shift)
    for i in range(len(letters_to_shift)):
        try:
            letter = letters_to_shift[i + t_shift]
        except IndexError:
            letter = letters_to_shift[i]
        finally:
            shifted_list.append(letter)
    for i in range(t_shift):
        if letters_to_shift[i] in shifted_list:
            break
        shifted_list.append(letters_to_shift[i])
    return shifted_list


def encode(word: str, shift: int) -> str:
    shifted_list = shifted(letters, shift)
    encoded = []
    for letter in word:
        if letter == " ":
            encoded.append("#")  # we use "#" to represent spaces in the encoded string
        else:
            index = letters.index(letter)
            encoded.append(shifted_list[index])
    return to_string(encoded)


def decode(word: str, shift: int) -> str:
    shifted_list = shifted(letters, shift)
    decoded = []
    for letter in word:
        if letter == "#":
            decoded.append(" ")  # we replace "#" with a space character in the decoded string
        else:
            index = shifted_list.index(letter)
            decoded.append(letters[index])
    return to_string(decoded)


x = encode(word="idrissa rusongeka", shift=3)
print(x)
print(decode(word=x, shift=3))
