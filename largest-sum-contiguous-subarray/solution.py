def find_solution(l):
    max_sum = 0
    current_sum = 0
    for i in l:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == '__main__':
    assert find_solution([-3, -4, 5, -1, 2, -4, 6, -1]) == 8
    assert find_solution([-2, 3, -1, 2]) == 4
