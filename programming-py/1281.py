def subract_product_and_sum(n):
    product, sum = 1, 0
    for each in str(n):
        product *= int(each)
        sum += int(each)
    return product - sum


# test below
print(subract_product_and_sum(234))
print(subract_product_and_sum(4421))
