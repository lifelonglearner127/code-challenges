def is_valid(s):
    stack = []
    opening_brackets = set('({[')
    closing_brackets = set(')}]')
    pair = {'}': '{', ')': '(', ']': '['}
    for i in s:
        if i in opening_brackets:
            stack.append(i)
        if i in closing_brackets:
            if not stack:
                return False
            elif stack.pop() != pair[i]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_valid('(){}[]') is True
    assert is_valid('(({[]}))') is True
    assert is_valid('()}[]') is False