def find_solution(l, sum_):
    start = 0
    length = len(l)
    current_sum = l[0]
    i = 1
    while i <= length:
        while current_sum > sum_ and start < i - 1:
            current_sum -= l[start]
            start += 1
        if current_sum == sum_:
            return [start, i - 1]
        if i < length:
            current_sum += l[i]
        i += 1


if __name__ == '__main__':
    assert find_solution([1, 4, 20, 3, 10, 5], 33) == [2, 4]