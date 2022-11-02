def find_permutation(text, l, r):
    if l == r:
        print("".join(text))
    for i in range(l, r):
        text[i], text[l] = text[l], text[i]
        find_permutation(text, l + 1, r)
        text[i], text[l] = text[l], text[i]


if __name__ == '__main__':
    text = list('ABC')
    find_permutation(text, 0, 3)
