def defangIP(address):
    defanged_ip = ""
    for each in address:
        if each == ".":
            defanged_ip += "[.]"
        else:
            defanged_ip += each
    return defanged_ip


# test below
print(defangIP("192.168.1.1"))
