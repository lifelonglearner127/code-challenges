def find_solution(l):
    length = len(l)
    total_sum = (length + 1) * (length + 2) // 2
    return total_sum - sum(l)


if __name__ == '__main__':
    assert find_solution([1, 2, 4, 6, 3, 7, 8]) == 5
