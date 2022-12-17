def eval_rpn(tokens):
    """ Valid Operators: + - * / """
    collector = []
    operators = ['+', '-', '*', '/']
    for each in tokens:
        if each in operators:
            num2 = collector.pop()
            num1 = collector.pop()
            if each == '+':
                collector.append(num1 + num2)
            elif each == '-':
                collector.append(num1 - num2)
            elif each == '*':
                collector.append(num1 * num2)
            else:
                collector.append(int(num1 / num2))
        else:
            collector.append(int(each))
    return collector[0]


# test below
print(eval_rpn(["2", "1", "+", "3", "*"]))
print(eval_rpn(["4", "13", "5", "/", "+"]))
print(eval_rpn(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))
