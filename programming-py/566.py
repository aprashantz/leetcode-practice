def matrix_reshape(mat, r, c):
    if len(mat) * len(mat[0]) != r * c:
        return mat
    desired_shaped_mat = [[0 for i in range(c)] for i in range(r)]
    flat_array = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            flat_array.append(mat[i][j])
    index_of_val_to_send = 0
    for i in range(r):
        for j in range(c):
            desired_shaped_mat[i][j] = flat_array[index_of_val_to_send]
            filled_output += 1
    return desired_shaped_mat


# test below
print(matrix_reshape([[1, 2], [3, 4]], 1, 4))
print(matrix_reshape([[1, 2], [3, 4]], 2, 4))
