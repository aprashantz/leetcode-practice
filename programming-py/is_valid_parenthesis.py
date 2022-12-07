def is_valid_bracket(string):
    open_parenthesis_stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for paranthesis in string:
        if paranthesis in mapping.values():
            open_parenthesis_stack.append(paranthesis)
        elif open_parenthesis_stack and mapping[paranthesis] == open_parenthesis_stack[-1]:
            open_parenthesis_stack.pop()
        else:
            return False
    return open_parenthesis_stack == []


# test below
print(is_valid_bracket("{[]}"))
