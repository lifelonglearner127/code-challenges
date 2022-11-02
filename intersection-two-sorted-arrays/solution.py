def find_solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    i = j = 0
    result = []
    while i < arr1_len and j < arr2_len:
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
    return result


if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = [1,3,5,6]
    assert find_solution(arr1, arr2) == [1, 3, 5]
