def find_solution(l):
    total_sum = sum(l)
    left_sum = 0
    for i, element in enumerate(l):
        total_sum -= element
        if left_sum == total_sum:
            return i
        left_sum += element
    return -1


if __name__ == '__main__':
    assert find_solution([-7, 1, 5, 2, -4, 3, 0]) == 3
    assert find_solution([1, 2, 3]) == -1
