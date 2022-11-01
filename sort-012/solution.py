def sort012(l):
    length = len(l)
    li = 0
    mi = 0
    ri = length - 1
    while mi <= ri:
        if l[mi] == 0:
            l[li], l[mi] = l[mi], l[li]
            li += 1
            mi += 1
        elif l[mi] == 1:
            mi += 1
        else:
            l[mi], l[ri] = l[ri], l[mi]
            ri -= 1
    return l


if __name__ == '__main__':
    assert sort012([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
    assert sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
