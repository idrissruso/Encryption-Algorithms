from typing import List

letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's',
           'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', "#"]  # we add "#" to represent spaces


def to_string(letters_list: list) -> str:
    return "".join(letters_list)


def shifted(letters_to_shift: List, shift: int) -> List[str]:
    shifted_list = []
    absolute_shift = shift if shift <= len(letters_to_shift) else shift - len(letters_to_shift)  # mode
    for i in range(len(letters_to_shift)):
        try:
            letter = letters_to_shift[i + absolute_shift]
        except IndexError:
            letter = letters_to_shift[i]
        finally:
            shifted_list.append(letter)
    for i in range(absolute_shift):
        if letters_to_shift[i] in shifted_list:
            break
        shifted_list.append(letters_to_shift[i])
    return shifted_list
