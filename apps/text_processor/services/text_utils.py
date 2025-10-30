from random import shuffle


def shuffle_word(word: str) -> str:
    if len(word) <= 3:
        return word
    middle = list(word[1:-1])
    shuffle(middle)
    return word[0] + "".join(middle) + word[-1]


def process_text(text: str) -> str:
    words = text.split()
    return " ".join(shuffle_word(w) for w in words)
