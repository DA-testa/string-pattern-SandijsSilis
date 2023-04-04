#


def read_input():
    in_type = input()

    if 'I' in in_type:
        pattern = input()
        text = input()

    if 'F' in in_type:
        filename = "./tests/06"
        with open(filename, mode="r") as fails:
            pattern = fails.readline()
            text = fails.readline()

    return (pattern.rstrip(), text.rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    res = []
    pat_h = 0
    lent = len(text)
    lenp = len(pattern)

    for char in pattern:
        pat_h = pat_h * 256 + ord(char)

    for i in range(lent-lenp+1):
        sub_h = 0
        subs = text[i:i+lenp]

        for char in subs:
            sub_h = sub_h * 256 + ord(char)

        if sub_h == pat_h and subs == pattern:
            res.append(i)
    return res


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

