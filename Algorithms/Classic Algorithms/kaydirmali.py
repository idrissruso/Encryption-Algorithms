from utils import to_string, letters, shifted


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



