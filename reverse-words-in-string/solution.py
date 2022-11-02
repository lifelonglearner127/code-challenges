def find_solution(s):
    words = s.split()
    return " ".join(words[::-1])


if __name__ == '__main__':
    assert find_solution("geeks quiz practice code") == "code practice quiz geeks"
    assert find_solution("getting good at coding needs a lot of practice") == "practice of lot a needs coding at good getting"
