def find_solution(prices):
    max_price = max(prices)
    profit = 0
    days_long = 0
    while len(prices) > 0:
        day_price = prices.pop(0)
        if day_price == max_price:
            profit += day_price * days_long
            days_long = 0
            if len(prices):
                max_price = max(prices)
        elif day_price < max_price:
            profit -= day_price
            days_long += 1
    return profit


if __name__ == '__main__':
    assert find_solution([5, 3, 2]) == 0
    assert find_solution([1, 2, 100]) == 197
    assert find_solution([1, 3, 1, 2]) == 3
