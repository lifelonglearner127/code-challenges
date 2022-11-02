def find_solution(l):
    solution = []
    length = len(l)
    max_right = l[-1]
    solution.append(max_right)
    for i in range(length - 2, -1, -1):
        if l[i] > max_right:
            max_right = l[i]
            solution.append(max_right)
    return solution


if __name__ == '__main__':
    assert set(find_solution([16, 17, 4, 3, 5, 2])) == {17, 5, 2}
