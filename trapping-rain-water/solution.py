def get_water_amount(l):
    result = 0
    for i in range(1, len(l) - 1):
        left_water_level = max(l[0:i])
        right_water_level = max(l[i+1:])
        water_level = min(left_water_level, right_water_level)
        result += water_level - l[i]
    return result


if __name__ == '__main__':
    assert get_water_amount([2, 1, 2]) == 1
    assert get_water_amount([3, 1, 2, 1, 4]) == 5
