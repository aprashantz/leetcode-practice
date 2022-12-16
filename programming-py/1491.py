def average_salary(salary):
    return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


# test below
print(average_salary([4000, 3000, 1000, 2000]))
