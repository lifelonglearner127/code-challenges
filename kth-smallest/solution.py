def find_solution(arr, k):
    arr.sort()
    return arr[k - 1]


if __name__ == '__main__':
    assert find_solution([7, 10, 4, 3, 20, 15], 3) == 7
    assert find_solution([7, 10, 4, 3, 20, 15], 4) == 10
