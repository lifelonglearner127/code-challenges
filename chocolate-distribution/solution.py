def find_solution(arr, m):
    length = len(arr)
    if m == 0 or length == 0:
        return 0
    if m > length:
        return -1
    arr.sort()
    min_diff = arr[-1] - arr[0]
    for i in range(length - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    return min_diff


if __name__ == '__main__':
    assert find_solution([7, 3, 2, 4, 9, 12, 56], 3) == 2
    assert find_solution([3, 4, 1, 9, 56, 7, 9, 12], 5) == 6
    assert find_solution([12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50], 7) == 10
