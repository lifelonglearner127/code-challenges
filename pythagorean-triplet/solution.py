import math


def find_solution(arr):
    arr.sort()
    length = len(arr)
    for i in range(length):
        arr[i] **= 2
    for i in range(length - 1, 1, -1):
        lookup = set()
        for j in range(i - 1, 0, -1):
            diff = arr[i] - arr[j]
            if diff in lookup:
                return {
                    (math.sqrt(arr[i])),
                    (math.sqrt(arr[j])),
                    (math.sqrt(diff))
                }
            else:
                lookup.add(arr[j])


if __name__ == '__main__':
    assert set(find_solution([3, 1, 4, 6, 5])) == {3, 4, 5}
    assert find_solution([10, 4, 6, 12, 5]) is None
