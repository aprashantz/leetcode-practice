def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")


# test below
print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))
