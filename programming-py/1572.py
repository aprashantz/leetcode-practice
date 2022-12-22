def diagonal_sum(mat):
    primary_diag_sum, sec_diag_sum = 0, 0
    for i in range(len(mat)):
        primary_diag_sum += mat[i][i]
    for i in range(len(mat)):
        if i != len(mat)-i-1:
            sec_diag_sum += mat[i][len(mat)-i-1]
    return primary_diag_sum + sec_diag_sum


# test below
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 25
print(diagonal_sum([[1, 1, 1, 1], [1, 1, 1, 1],
      [1, 1, 1, 1], [1, 1, 1, 1]]))  # 8
print(diagonal_sum([[5]]))  # 5
