def find_indices(l, target):
    lookup = {}
    for i, n in enumerate(l):
        if target - n in lookup:
            return lookup[target - n], i
        else:
            lookup[n] = i


if __name__ == '__main__':
    assert set(find_indices([1, 2, 3, 4], 7)) == {3, 2}
