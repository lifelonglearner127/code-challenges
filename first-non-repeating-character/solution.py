from collections import Counter


def find_solution(s):
    counter = Counter(s)
    for letter in s:
        if counter[letter] == 1:
            return letter


if __name__ == '__main__':
    assert find_solution("GeeksforGeeks") == "f"
    assert find_solution("GeeksQuiz") == "G"
