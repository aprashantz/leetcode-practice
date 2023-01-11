def isValidSudoku(board):
    def isRepeated(flat_list):
        for each_cell in set(flat_list):
            if each_cell != ".":
                if flat_list.count(each_cell) > 1:
                    return True

    # first checking row validation
    for each_row in board:
        if isRepeated(each_row):
            return False

    # second checking column validation
    for col_index in range(9):
        each_col = []
        for row_index in range(9):
            each_col.append(board[row_index][col_index])
        if isRepeated(each_col):
            return False

    # third sub boxes validation
    for box_row_index in range(0, 9, 3):
        for box_col_index in range(0, 9, 3):
            each_sub_box = []
            for each_row_index in range(box_row_index, box_row_index+3):
                for each_col_index in range(box_col_index, box_col_index+3):
                    each_sub_box.append(board[each_row_index][each_col_index])
            if isRepeated(each_sub_box):
                return False

    return True


# test below
print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
