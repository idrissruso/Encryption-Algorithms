from typing import List
from utils import letters, to_sting


def shifted(letters_to_shift: List, shift: int) -> List[str]:
    shifted_list = []
    t_shift = shift if shift <= len(letters) else shift - len(letters)
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
        index = letters.index(letter)
        encoded.append(shifted_list[index])
    return to_sting(encoded)


def decode(word: str, shift: int) -> str:
    shifted_list = shifted(letters, shift)
    encoded = []
    for letter in word:
        index = shifted_list.index(letter)
        encoded.append(letters[index])
    return to_sting(encoded)


