'''Contains helper functions to avoid clutter in the main programs'''
# Get individual and total values of optimized boards.
def get_values(boards_optimized, assortment):
    board_values = []
    for board in boards_optimized:
        board_val = 0
        for section in board:
            if not isinstance(section[0], str):
                continue
            for type in assortment:
                if section[0] == type[1]:
                    board_val += type[3] 
        board_values.append(board_val)
    return board_values 


# Get length of the longest board in boards.
def get_board_lens(boards):
    board_lens = []
    for board in boards:
        board_lens.append(sum([x[1] for x in board]))
    return board_lens
