letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's',
           'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', "#"]  # we add "#" to represent spaces


def to_string(letters_list: list) -> str:
    return "".join(letters_list)
